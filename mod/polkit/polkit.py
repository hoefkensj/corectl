#!/usr/bin/env python
import os
import sys

def su():
	euid = os.geteuid()
	if euid != 0:
		print("Script not started as root. Running sudo..")
		args = ['sudo', sys.executable] + sys.argv + [os.environ]
		# the next line replaces the currently-running process with the sudo
		os.execlpe('sudo', *args)
		return
	else:
		return euid == 0