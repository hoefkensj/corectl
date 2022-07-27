# !/usr/bin/env python
#   Copyright (c)  2022  Hoefkens J (hoefkensj@gmail.com)
#
import os
import sys
import types

def lib_pkg(fn_name):
	def is_module(path):
		l = path
		try:
			with open(path, 'r') as f:
				l = f.readline()
			ismod = True if l.startswith('#!') and 'python' in l else False
		except IsADirectoryError:
			ismod = False
		# True if True in [True for item in os.listdir(path) if  item == "__init__.py" ] else False
		return ismod
	def is_pkg(path):
		"""
		:param path: path to test for it being a python package (has __init__.py)
		:return: boolean (true for is package false if not )
		# True if True in [True for item in os.listdir(dirpath) if  item == "__init__.py" ] else False =>>>
		# test = any([True for item in os.listdir(dirpath) if  item == "__init__.py" ]) =>>>
		"""
		return any(["__init__.py" in os.listdir(path)])
	def find_master():
		"""
		!!! warning breaks when __init__. is in everyfolder of the path up until /  !!!
		gets the folder(path) that is the highest up in the path that still is a python package
		"""
		pathself = sys.argv[0]
		pself = pathself
		parent_dir_pself = os.path.split(pself)[0]
		pdirps = parent_dir_pself
		lst_parent_folders_pself = pdirps.split('/')
		lst_pdps = lst_parent_folders_pself
		os.chdir(os.path.split(sys.argv[0])[0])
		master=[pkg[0] for pkg in ([path, pkg.is_pkg(path)] for path in ['/'.join(lst_pdps[:(len(lst_pdps) - idx)]) for idx, folder in enumerate(reversed(lst_pdps)) if os.path.exists('/'.join(lst_pdps[:(
			len(lst_pdps) - idx)]))][:-1]) if pkg[1] == True][-1]
		return master
	
	lib_fn = {
		'is_mod'     : is_module,
		'is_pkg'     : is_pkg,
		'find_master': find_master,
		}
	fn = lib_fn[fn_name]
	return fn

pkg = types.SimpleNamespace()
pkg.is_mod = lib_pkg('is_mod')
pkg.is_pkg = lib_pkg('is_pkg')
pkg.find_master = lib_pkg('find_master')

sprint = sys.stdout.write

def regx():
	import re
	
	def represets(preset):
		presetlib = {
			'sys'  : r'^(?P<DAT>{DAT})(?P<IDX>\d+)$',
			'sysfx': r'^(?P<DAT>{DAT})(?P<IDX>\d+)(?P<SEP>{SEP})(?P<SUF>{SUF})$',
			'tab'  : r'\t',
			'ansim': r'\x1b\[[;\d]*m',
			'full' : r'^(?P<DAT>{DAT})$',
			'subs' : r'^((.*)(?P<SUB>{sub})(.*))$',
			}
		return presetlib[preset]
	def revx(rExpr):
		def compyle(**k):
			exprt = rExpr.format(**k)
			return re.compile(f'{exprt}', re.VERBOSE)
		return compyle
	rx = types.SimpleNamespace()
	preset_sys = represets('sys')
	preset_full = represets('full')
	preset_sysfx = represets('sysfx')
	preset_subs = represets('subs')
	rx.sys = types.SimpleNamespace()
	rx.sysfx = types.SimpleNamespace()
	rx.full = types.SimpleNamespace()
	rx.subs = types.SimpleNamespace()
	rx.sys.cpl = revx(preset_sys)
	rx.full.cpl = revx(preset_full)
	rx.sysfx.cpl = revx(preset_sysfx)
	rx.subs.cpl = revx(preset_subs)
	rx.sys.cpu = rx.sys.cpl(DAT='cpu')
	rx.sys.hwmon = rx.sys.cpl(DAT='hwmon')
	rx.sysfx.temp = rx.sysfx.cpl(DAT='temp', SEP='_', SUF='.*')
	rx.full.coretemp = rx.full.cpl(DAT='coretemp')
	
	return rx

def tabs(n):
	return (n * '    ')

def ffix(ftype):
	case = {
		'f': '┣━ ',
		'd': '╋━━[/] '
		}
	return case[ftype]

def ls_pyod(path, flags=''):
	"""
	similar to the systems 'ls -A' lists directory contents
	:param path full system path of the dir to ls
	:return: the contents of the dir split in [python scripts], [other], [dirs]
	"""
	A = [name for name in os.listdir(path)]
	visible = [item for item in A if not item.startswith('.')]
	pyscrs = sorted([item for item in visible if item.endswith('.py')], key=str.casefold)
	dirs = sorted([item for item in visible if os.path.isdir(os.path.join(path, item))])
	dirs = [d for d in dirs if not d.startswith('__')]
	other = sorted([item for item in visible if item not in dirs and item not in pyscrs])
	other = [o for o in other if not o.startswith('__')]
	return [pyscrs, other, dirs]

def ls_A(path):
	A = list(os.listdir(path))
	li = []
	dirs = sorted([item for item in A if os.path.isdir(os.path.join(path, item))])
	li += dirs
	files = sorted([item for item in A if os.path.isfile(os.path.join(path, item))])
	li += files
	return li

def build_tree():
	pkgpath = pkg.find_master()
	pkgname = os.path.split(pkgpath)[-1]
	# contents = os.listdir(path)
	def get_contents(path):
		sall = ls_pyod(path)
		return sall[0], sall[1], sall[2]
	def sprint_files(path, childof):
		prefix = f'    {childof}{ffix("f")}'
		for file in get_contents(path)[0]:
			sprint(f'{prefix}{file}\n')
		for file in get_contents(path)[1]:
			sprint(f'{prefix}{file}\n')
	# sprint(f'{childof}|\n')
	def sprint_folder(path, childof, thisfolder):
		sprint(f'{childof}{ffix("d")}{thisfolder}\n')
		sprint_files(path, childof)
		childof += '│   '
		
		for idx, folder in enumerate(get_contents(path)[2]):
			sprint_folder(os.path.join(path, folder), childof, folder)
	# sprint(f'{childof}\n')
	# prefix=get_prefix('f',lvl+1)
	# sprint_pyscr(path,prefix)
	# sprint_other(path, prefix)
	sprint(f'\n#==>[~]\t\"\"\"\tPackage: [ \'{pkgname}\' ]\t\"\"\"')
	sprint(f'\n     ║')
	sprint(f'\n')
	path = pkgpath
	sprint_folder(pkgpath, "     ", pkgname)

def main():
	build_tree()

if __name__ == '__main__':
	main()

