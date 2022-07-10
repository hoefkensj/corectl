#!/usr/bin/env python
import os
import re
import sys

def regex_cpux():
	return re.compile('^cpu(\d+)$')




def read(file):
	file_content=[]
	with open(file,'r') as f:
		while True:
			content=f.readline()
			if content == "":
				break
			else:
				file_content+=content.split()
	return file_content
	
	
def init_cores():
	base_path='/sys/devices/system/cpu/'
	core_path='{base}{core}'
	core_prop='{corepath}{prop}'
	reg=regex_cpux()
	cores=[]
	tree={}
	for node in os.listdir(base_path):
		result=reg.search(node)
		if result:
			cores += [result.group()]
	cores.sort()
	
	for core in cores:
		tree[f'{core}']={}
		tree[f'{core}']['cpufreq']={}
		path=core_path.format(base=base_path,core=core)
		cpufreq_path=os.path.join(path,'cpufreq')
		for file in os.listdir(cpufreq_path):
			# tree[f'{core}']['cpufreq'][f'{file}']=
			file_path=os.path.join(cpufreq_path,file)
			content=read(file_path)
			tree[f'{core}']['cpufreq'][f'{file}']= content
	return tree
	
	


ident = 1


def print_dicttree(d, indent=0):
	for key, value in d.items():
		tabs='\t' * indent
		sys.stdout.write('\n')
		sys.stdout.write(tabs)
		sys.stdout.write(str(key))
		sys.stdout.write('\t')
		sys.stdout.flush()
		
	
		if isinstance(value, dict):
			print_dicttree(value, indent+1)
		else:
			tabs='\t' * (1)
			# sys.stdout.write(tabs)
			sys.stdout.write(str(value))
			sys.stdout.flush()
    
         
def print_dicttee(dct,ident):
	def testkey(content,ident):
		if isinstance(dct[key], dict):
			tabs = ident * '\t'
			sys.stdout.write(tabs)
			sys.stdout.write(key)
			sys.stdout.write('\n')
			sys.stdout.flush()

			ident+=1
			print_dicttee(dct[key], ident)
			
		else:
			tabs = ident * '\t'
			sys.stdout.write(tabs)
			sys.stdout.write(key)
			sys.stdout.write('\t:\t')
			sys.stdout.write(str(dct[key]))
			sys.stdout.write('\n')
			sys.stdout.flush()
			
			
	for key in dct.keys():

		testkey(dct[key],ident)

		


		
		
cores=init_cores()
print_dicttree(cores,ident)
	
	
	# cores= [iscpu.group()  if iscpu.match(node)]
	
	# coress=[print() for node in os.listdir(base_path) ]
	# print(cores.sort())
	#
	# for core in cores:
	# 	tree[f'{core}']={}
	#
	# for core in tree.keys():
	# 	tree[core]=[os.listdir(core_path.format(base=base_path,core=core))]
	# 	for  prop in tree[core]:
	# 		tree[core]={}
	# 		tree[core][f'{prop}']=read(core_prop.format(corepath=core_path.format(base=base_path,core=core),prop=prop))
	# 	print(tree[core])
		
	# 		os.listdir(core_path.format(base=base_path,core=core)):} for core in  cores}
	#
	# for core in tree.keys():
	# 	print(core)
	# 	print(tree[core])
	#
	#
	# tree={os.path.join(base_path,node) : read(node) for node  in nodes if os.path.isfile(os.path.join(base_path,node)) }
	# # links=[os.path.join(base_path,node)  for node  in nodes if os.path.islink(os.path.join(base_path,node)) ]
	# tree+={os.path.join(base_path,node): os.listdir(base_path) for node  in nodes if os.path.isdir(os.path.join(base_path,node))}
	
	
	# for folder in folders:
	# 	files += [os.path.join(base_path,folder,node) for node in nodes if os.path.isfile(os.path.join(base_path,folder,node))]
	# 	links += [os.path.join(base_path,folder,node) for node in nodes if os.path.islink(os.path.join(base_path,folder, node))]
	# 	folders += [os.path.join(base_path,folder,node) for node in nodes if os.path.isdir(os.path.join(base_path,folder,node))]
	#
	# 	print(files)
	# # 	print(links)
	# # 	print(folders)
	# # 	for file in files:
	# 		print(file,':\t',)


# def read_scalinggovernor():
# 	count_cores
# 	for core in cores:
# 	cpu_path=f'/sys/devices/system/cpu/cpufreq/policy{core}'
# 	r = read_file("/sys/devices/system/cpu/cpu%d/cpufreq/scaling_governor" % cpu)
# 		if r is None:
# 			return "Unknown"
# 		else:
# 			return r[:-1]
# 	else:
# 		return "Disabled"