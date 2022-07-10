#!/usr/bin/env python
import os
import re
import sys
import cpuinfo
def cpu_info():
	cpuid= cpuinfo.get_cpu_info()
	return cpuid
def mkpath(**k):
	skel ='/sys/devices/system/cpu/{core}{mod}{file}'
	path=skel.format(
										core=k.get('core')  or '',
										mod=k.get('mod')  or '',
										file=k.get('file') or '',)
	return path

def init():
	def cores():
		cores = {}
		str_core = re.compile('^cpu(\d+)$')
		for item in os.listdir(mkpath()):
			if str_core.fullmatch(item):
				cores[item] = {'paths' : {'core': mkpath(core=item),}}
		return sorted(cores)
	
	def frqs(cpu):
		fls = [
			'base_frequency',
			'cpuinfo_max_freq',
			'cpuinfo_min_freq',
			'cpuinfo_transition_latency',
			'energy_performance_available_preferences',
			'energy_performance_preference',
			'scaling_available_governors',
			'scaling_cur_freq',
			'scaling_driver',
			'scaling_governor',
			'scaling_max_freq',
			'scaling_min_freq',
			'scaling_setspeed',
			]
		for c in cpu.keys():
			p ={f'{f}': str(mkpath(core=c, mod='/cpufreq/', file=f)) for f in fls}
			
			cpu[c]['paths']['frqs'] = p
		return cpu
	
	
	lst_cores=cores()
	dctmin={'paths' : {},}
	dct_cores={core : dctmin for core in lst_cores }
	socket0={
		'cpu' : {
							'cpuid': cpu_info(),
							'cores': dct_cores,
		}
		}
	



	socket0['cpu']['cores']=frqs(socket0['cpu']['cores'])
	return socket0




	# cpuinfo = list()
	#
	# # Append all CPUs to the list
	# try:
	# 	cpus = os.listdir("/sys/devices/system/cpu/cpufreq")
	# 	for cpu in cpus:
	# 		if "policy" in cpu:
	# 			cpu = dict()
	# 			cpu["name"] = "Disabled"
	# 			cpu["id"] = "unknown"
	# 			cpu["core"] = "unknown"
	# 			cpu["vendor"] = "unknown"
	# 			cpu["cache"] = 0
	# 			cpu["driver"] = driver(len(cpuinfo))
	# 			cpuinfo.append(cpu)
	# except (OSError, IOError) as err:
	# 	print("[CPUFace] Unable to get CPU information")
	# 	exit(2)



# def stdw_dct(dct):
	# for key in dct.keys():
	# 	sys.stdout.write(key)
	# 	sys.stdout.write('\n\t')
	# 	for subkey in dct[key].keys():
	# 		sys.stdout.write(subkey)
	# 		sys.stdout.write('\t:\t')
	# 		for subsubkey in dct[key][subkey].keys():
	# 			sys.stdout.write('\n\t\t')
	# 			sys.stdout.write(subsubkey)
	# 			sys.stdout.write('\t:\t')
	# 			for subsubsubkey in dct[key][subkey][subsubkey].keys():
	# 				sys.stdout.write('\n\t\t')
	# 				sys.stdout.write(subsubsubkey)
	# 				sys.stdout.write('\t:\t')
	# 			sys.stdout.write(dct[key][subkey][subsubkey][subsubsubkey])
	#
	# 		sys.stdout.write('\n')
	# 	sys.stdout.write('\n')
	# 	sys.stdout.flush()
	
	
	
def stdw_dct(d, indent=0):
	for key in d.keys():
		if isinstance(d[key], dict):
			sys.stdout.write('  |  ' * (indent)+'  |--' + str(key) + ':\n')
			stdw_dct(d[key], indent + 1)
		else:
			sys.stdout.write('  |  ' * (indent)+'  |--' +str(key) +'\t:\t'+ str(d[key])+'\n')



socket0=init()
print(sorted(socket0['cpu']['cores'].keys()))
stdw_dct(socket0)

