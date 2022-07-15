#!/usr/bin/env python
import os
import sys
import pickle


def home():
	return os.path.split(os.path.realpath(__file__))[0]

def testenv(**k):
	n = k['n'];
	h = k['h'];
	m = k['m']
	[[print('\033[0m{n}\033[32m{k}={v}\033[0m'.format(n=n, v="\n".join([f'\033[0m', *os.environ.get(c).split(":")]), k=c)) for c in os.environ.keys() if t in c.casefold()] for t in h]
	[print(f'{n}:\033[31m {v} : FAIL!\033[0m') for v in m if not os.environ.get(v)]

def super_su(**k):
	helper = k.get('su')

	python, script = sys.executable, sys.argv
	PYPATHORG = os.environ.get('PYTHONPATH')
	PYPATHPYX = os.path.dirname(os.path.dirname(python))
	PYPATHSCR = os.path.dirname(script[0])
	PYPATHPKG = os.path.dirname(os.path.dirname(script[0]))
	PYTHONPATH = '{}:{}:{}:{}'.format(PYPATHORG, PYPATHPYX, PYPATHSCR, PYPATHPKG)
	os.environ['PYTHONPATH'] = PYTHONPATH
	env = os.environ
	args = [helper, python] + script  # + [os.environ]
	os.execvpe(helper, args, os.environ)

def env_load():
	with open('/tmp/REROOT_USER.env', 'rb') as f:
		env_tmp = pickle.load(f)
	# only add keys that are missing, avoids overwriting USER ,USERHOME , ...
	os.environ = {key: env_tmp[key] for key in env_tmp.keys() if key not in os.environ.keys()}

def env_store():
	with open('/tmp/REROOT_USER.env', 'wb') as f:
		pickle.dump({**os.environ}, f)