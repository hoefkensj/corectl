#!/usr/bin/env python
import os
import re
import sys
import cpuinfo

def read(file):
	file_content = []
	with open(file, 'r') as f:
		while True:
			content = f.readline()
			if content == "":
				break
			else:
				file_content += content.split()
	return file_content






def socket0(p=''):
	p = '/sys/devices/system/cpu'
	def cpu_info():
		cpuid = cpuinfo.get_cpu_info()
		return cpuid
		
	def cores(**k):
		rx = re.compile('^cpu(\d+)$')
		cores = [rx.search(node).group() for node in os.listdir(p) if rx.search(node)]
		dct= {core : {	'path' : f'{p}/{core}', } for core in cores}
		keys=sorted(dct.keys())
		cores= {key: dct[key] for key in keys}
		
		return cores
	
	def frqs():
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
		dct_cores={}
		pfrq = f'{p}/cpufreq'
		rx = re.compile('(^policy(?P<n>\d+)$)')
		for node in os.listdir(pfrq):
			n = rx.search(node)
			core= f'cpu{n.group("n")}'
			ppol=f'{pfrq}/{n.group(0)}'
			ppol_props={prop : { 'path' : f'{ppol}/{prop}',
                           'value' : read(os.path.join(ppol,prop))} for prop in fls}
													 

			dct_core= { 'cpufreq' : ppol_props}
			dct_cores[core]=dct_core
		return dct_cores
		
	
	socket0 = {
		'cpu': {
			'cpuid': cpu_info(),
			'cores': cores(),
			}
		}
	cpufreq= frqs()
	for key in socket0['cpu']['cores'].keys():
		socket0['cpu']['cores'][key] = { **socket0['cpu']['cores'][key],**cpufreq[key]}
	
	return socket0

def print_dicttree(dct, ident):
	def testkey(content, ident):
		if isinstance(dct[key], dict):
			tabs = ident * '\t'
			sys.stdout.write(tabs)
			sys.stdout.write(key)
			sys.stdout.write('\n')
			sys.stdout.flush()
			
			ident += 1
			print_dicttree(dct[key], ident)
		
		else:
			tabs = ident * '\t'
			sys.stdout.write(tabs)
			sys.stdout.write(key)
			sys.stdout.write('\t:\t')
			sys.stdout.write(str(dct[key]))
			sys.stdout.write('\n')
			sys.stdout.flush()
	for key in dct.keys():
		testkey(dct[key], ident)

# socket0 = socket0()
# print_dicttree(socket0, 0)

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


# print(socket0['cpu']['cores']['cpu0']['cpufreq']['scaling_available_governors']['value'])


# stdw_dct(socket0)

