#!/usr/bin/env python
import os
import sys
import re

def presets_re():
	import types
	import re
	preset = types.SimpleNamespace()
	preset.repl_ANSIm = re.compile(r'\033\[[;\d]*m',re.VERBOSE).sub
	preset.repl_ESCt = re.compile(r'\t',re.VERBOSE).sub
	return preset

def re_escn(**k): return re.compile

def read1l(p):
	with open(p, 'r') as f:
		f=f.readline()
	return f

