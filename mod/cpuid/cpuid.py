#!/usr/bin/env python
import os
import re
import sys
import types
def read_file(path):
	content = []
	with open(path) as f:
		c=f.readlines()
	return c

def read_sysfs(path):
	with open(path) as f:
		c=f.readline().strip()
	return c

def read_rtval(path):
	def rtval():
		return read_sysfs(path)
	return rtval
	
def regx():
	def represets(preset):
		presetlib = {
			'sys'     : r'^(?P<DAT>{DAT})(?P<IDX>\d+)$',
			'sysfx'   : r'^(?P<DAT>{DAT})(?P<IDX>{IDX})(?P<SEP>{SEP})(?P<SUF>{SUF})$',
			'syscore' : r'^(?P<DAT>{DAT})(?P<SEP>{SEP})(?P<IDX>{IDX})$',
			'tab'     : r'\t',
			'ansim'   : r'\x1b\[[;\d]*m',
			'full'    : r'^(?P<DAT>{DAT})$',
			'kv'      : r'^(?P<KEY>{KEY})(?P<SEP>{SEP})(?P<VAL>{VAL})$',
			'subs'    : r'^((.*)(?P<SUB>{sub})(.*))$',
			'repl'    : r'{SUB}',
			}
		return presetlib[preset]
	def revx(rExpr):
		def compyle(**k):
			exprt = rExpr.format(**k)
			return re.compile(f'{exprt}', re.VERBOSE)
		return compyle
	
	def repl(rExpr):
		def compyle(**k):
			exprt = rExpr.format(**k)
			return re.compile(f'{exprt}', re.VERBOSE).sub
		return compyle
	
	rx = types.SimpleNamespace()
	preset_sys 		= represets('sys')
	preset_full 	=	represets('full')
	preset_sysfx 	= represets('sysfx')
	preset_syscore 	= represets('syscore')
	preset_subs 	= represets('subs')
	preset_kv 		= represets('kv')
	preset_repl		=	represets('repl')
	rx.sys 			= types.SimpleNamespace()
	rx.sysfx 		= types.SimpleNamespace()
	rx.syscore 	= types.SimpleNamespace()
	rx.full 		= types.SimpleNamespace()
	rx.subs 		= types.SimpleNamespace()
	rx.kv 			= types.SimpleNamespace()
	rx.repl			=	types.SimpleNamespace()
	rx.sys.cpl 		= revx(preset_sys)
	rx.full.cpl 	= revx(preset_full)
	rx.sysfx.cpl 	= revx(preset_sysfx)
	rx.syscore.cpl 	= revx(preset_syscore)
	rx.subs.cpl 	= revx(preset_subs)
	rx.kv.cpl 		= revx(preset_kv)
	rx.repl.cpl		=	repl(preset_repl)
	rx.sys.cpu 					= rx.sys.cpl(DAT='cpu')
	rx.sys.policy 			= rx.sys.cpl(DAT='policy')
	rx.sys.thermal_zone	= rx.sys.cpl(DAT='thermal_zone')
	rx.sys.hwmon 				= rx.sys.cpl(DAT='hwmon')
	rx.sysfx.temp 			= rx.sysfx.cpl(DAT='temp', IDX='\d+',SEP='_', SUF='.*')
	rx.syscore.core			= rx.syscore.cpl(DAT='Core', SEP='\s', IDX='\d+',)
	rx.syscore.pkg 			= rx.syscore.cpl(DAT='Package', SEP='\sid\s', IDX='\d+', )
	rx.full.coretemp 		= rx.full.cpl(DAT='coretemp')
	rx.kv.processor 		= rx.kv.cpl(KEY='processor', SEP=':', VAL='\d+')
	rx.kv.keyval 				= rx.kv.cpl(KEY='.*?', SEP=':', VAL='.*?')
	rx.repl.space				= rx.repl.cpl(SUB="\s")
	
	return rx

def cpu():
	def cpuinfo():
		blocks = {}
		cpuinfo = {}
		n = 0
		blocks[n] = {}
		with open('/proc/cpuinfo') as f:
			f = f.readlines()
		for line in f:
			if line == '\n':
				n += 1
				blocks[n] = {}
			else:
				keyval = rx.kv.keyval.search(line)
				key = keyval.group('KEY').strip()
				key = rx.repl.space('-', key)
				val = keyval.group('VAL').strip()
				blocks[n][key] = val
		for block in blocks:
			core = blocks[block].get('processor')
			if core:
				cpuinfo[int(core)] = blocks[block]
		return cpuinfo

	def cpufrq():
		fls = ['base_frequency', 'cpuinfo_max_freq', 'cpuinfo_min_freq', 'cpuinfo_transition_latency', 'energy_performance_available_preferences', 'energy_performance_preference', 'scaling_available_governors', 'scaling_cur_freq', 'scaling_driver', 'scaling_governor', 'scaling_max_freq', 'scaling_min_freq', 'scaling_setspeed']

		dct_cores = {}
		pfrq = '/sys/devices/system/cpu/cpufreq'
		for node in os.listdir(pfrq):
			n = rx.sys.policy.search(node)
			core = int(n.group('IDX'))
			ppol = f'{pfrq}/{n.group(0)}'
			ppol_props = {prop: {'path': f'{ppol}/{prop}', 'rtval': read_rtval(os.path.join(ppol, prop)), 'value': read_sysfs(os.path.join(ppol, prop))} for prop in fls}

			dct_core = ppol_props
			dct_cores[core] = dct_core
		cpufreq = {'path': pfrq, 'freq': dct_cores}
		return cpufreq

	def coregroups(info):
		grouplist = []
		for idx, core in enumerate(sorted(info.keys())):
			grouplist += [int(info[core]['core-id'])]
		return grouplist

	def hwmon():
		path_hwmon = '/sys/class/hwmon/'
		path_coretemp = ''
		sensors = {}
		def coretemp(sensors, path_hwmon):
			sensors['coretemp'] = {}
			params_coretemp = {}
			path_coretemp = ''
			def find_coretemp(path_coretemp, path_hwmon):
				dirlist_hwmon = sorted(os.listdir(path_hwmon))
				for idx, mon in enumerate(dirlist_hwmon):
					name = read_sysfs(os.path.join(path_hwmon, mon, 'name'))
					if name == 'coretemp':
						path_coretemp = os.path.realpath(os.path.join(path_hwmon, mon))
				return path_coretemp

			def read_coretemps(params, path_coretemp):
				resort = {}
				for file in sorted(os.listdir(path_coretemp)):
					rex = rx.sysfx.temp.search(file)
					if rex:
						idx = int(rex.group('IDX'))
						idn = rex.group('SUF')
						path = os.path.realpath(os.path.join(path_coretemp, file))
						if idx not in params.keys():
							params[idx] = {}
						else:
							params[idx][idn] = {'path': path, 'rtval': read_rtval(path), 'value': read_sysfs(path)}

				for coretemp in params.keys():
					label = params[coretemp]['label']['value']
					rexp = rx.syscore.pkg.search(label)
					if rexp:
						idxp = int(rexp.group('IDX'))
						pkg = params[coretemp]
					rexc = rx.syscore.core.search(label)
					if rexc:
						idxc = int(rexc.group('IDX'))
						resort[idxc] = params[coretemp]
				params = {'package': pkg, 'cores': resort}
				return params

			path_coretemp = find_coretemp(path_coretemp, path_hwmon=path_hwmon)
			params_coretemp = read_coretemps(params_coretemp, path_coretemp=path_coretemp)
			sensors['coretemp'] = {'path': path_coretemp, 'temps': params_coretemp}
			return sensors

		sensors = coretemp(sensors, path_hwmon=path_hwmon)
		hwmon = {'coretemp': sensors['coretemp']}
		return hwmon

	def cpucores(syfs_path):
		cores = []
		for node in os.listdir(syfs_path):
			if rx.sys.cpu.search(node):
				cores.append(rx.sys.cpu.search(node).group())
		return sorted(cores)

	p = "/sys/devices/system/cpu"
	rx = regx()
	cpucores = cpucores(p)
	cores_cpuinfo = cpuinfo()
	cores_cpufreq = cpufrq()
	cores_hwmon = hwmon()
	coregroup = coregroups(cores_cpuinfo)
	
	cores = {
		i	: {
			'meta'		: {	'sysfs'	: os.path.join(p, core),},
			'cpufreq'	:	{	**cores_cpufreq['freq'][i]			},
			'hwmon'		: {
				'coretemp'	:	{
					'core-id'			:		f'{coregroup[i]}',
					'parameters'	: 	{	**cores_hwmon['coretemp']['temps']['cores'][coregroup[i]]	},
											},
									},
			'cpuinfo': cores_cpuinfo[i]
				} for i, core in enumerate(cpucores)
				}


	cpu = {'package': {'meta': {'sysfs': p}, 'temp': cores_hwmon['coretemp']['temps']['package']}, 'cores': {**cores}}

	fn_rtfreq = {c: cores[c]["cpufreq"]["scaling_cur_freq"]["rtval"] for c in cores}


	fn_rttemp = {c: cores[c]['hwmon']['coretemp']['parameters']['input']['rtval'] for c in cores}


	fnrt = {'freq': fn_rtfreq, 'temp': fn_rttemp}
	cpu['fn'] = fnrt
	pkg_id = cpu['package']['temp']['label']['value']
	rexp = rx.syscore.pkg.search(pkg_id)
	id = rexp.group('IDX')
	cpudata = {id: {**cpu}}
	return cpudata

def print_dicttree(dct, ident):
	def testkey(content, ident):
		if isinstance(dct[key], dict):
			tabs = ident * '\t'
			sys.stdout.write(tabs)
			sys.stdout.write(str(key))
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

def stdw_dct(d, indent=0):
	for key in d.keys():
		if isinstance(d[key], dict):
			sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + '\x1b[1;32m'+str(key) + ':' +'\x1b[0m\n')
			stdw_dct(d[key], indent + 1)
		else:
			sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + str(key) + '\t:\t' + str(d[key]) + '\n')

if __name__ == '__main__':
	cpu = cpu()
	stdw_dct(cpu)
# 	cores_ponline="/sys/devices/system/cpu/online"
# 	cores_poffline="/sys/devices/system/cpu/offline"
#\

	# print(cpu['cpu']['temp']['package']['input']['rtval']())
