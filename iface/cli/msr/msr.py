#!/usr/bin/env python
import click as C
import func.msr


@C.group()
@C.pass_context
def msr(ctx):
	"""Throttlestop : \n Control MSR: BiDirectional Processor Hot"""

	# ensure that ctx.obj exists and is a dict (in case `cli()` is called
	# by means other than the `if` block below)

	ctx.ensure_object(dict)
	func.main.su()

@msr.command()
def list():
	"""list known MSR Flags"""
	pass
	
@msr.command()
def read():
	"""read flag from msr"""

def write():
	"""write flag to msr"""
	pass
	
@msr.command()
def clear():
	"""clear flag in msr (set to 0)"""
	
@msr.command()
def set():
	"""set flag in msr (set to 1)"""
	