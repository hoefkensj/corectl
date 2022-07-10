#!/usr/bin/env python
import mod.msr.msr

def known_flags():
	flags={}
	flags['BD_PROCHOT']={
													'register' 	: 0x1FC,
													'bit'				:	0
											}


def read_flag(*a,**k):
	flag=k.get('flag')
	flags={
		'BD_PROCHOT' : mod.msr.msr.read_BDPROCHOT()
	}
	return flags['flag']
	