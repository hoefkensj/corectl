setSpacing(0)#!/usr/bin/env python

	
	
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