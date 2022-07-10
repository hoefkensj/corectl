#!/usr/bin/env python

import func.proc
import func.msr
import func.stdfn
import static.locale
import func.msr
import itrface.cli.clo

INFO=static.locale.loadloc('en')['cli']['main']['info']


@C.group()
@C.option('-y',	'--yes'			,	'y'				, is_flag=True, help=INFO['opt_y'])
@C.option('-s',	'--script'	,	'script'	, is_flag=True, help=INFO['opt_y'])
@C.option('-m',	'--minimal'	,	'stdout'	,	is_flag=True,	help=INFO['opt_y'],flag_value='m',)
@C.option('-#',	'--hex'			,	'stdout'	,	is_flag=True,	help=INFO['opt_y'],flag_value='h',)
@C.option('-b',	'--bool'		,	'stdout'	,	is_flag=True,	help=INFO['opt_y'],flag_value='b',)
@C.option('-t',	'--table'		,	'table'		,	default='fancy',help=INFO['opt_y'])
@C.pass_context
def entry_point(ctx,y,script,stdout,table):
	"""Throttlestop : \n Control MSR: BiDirectional Processor Hot"""

	# ensure that ctx.obj exists and is a dict (in case `cli()` is called
	# by means other than the `if` block below)

	ctx.ensure_object(dict)
	func.main.su()


@C.command()
@C.pass_context
@C.argument('flag')
def read(ctx,flag):
	"""Check MSR: 0x1FC[0]"""
	func.msr.read_flag(flag='BD_PROCHOT')
	data=[rq
				['  MSR #0x1FC',check,]
	]
	# std_out=func.stdfn.std_row(check,'MSR #0x1FC' ,2)
	# C.echo([f'{it}\n' for it in std_out])
	stdout_str=itrface.cli.clo.stdout_table(ctx.parent.params['table'])
	C.echo(stdout_str(data).format(placeholderw16=f"{row[1]['HEXX'][:-4]}\x1b[1;32m{row[1]['HEXX'][-4:]}\x1b[0m"))

@C.command()
@C.pass_context
@C.argument('flag')
def set(ctx,flag):
	"""Set BD_PROCHOT Flag (set to 1)"""

	return
	
@C.command()
@C.pass_context
def clear(ctx):
	"""Clear BD_PROCHOT Flag (set to 0)"""
	
	return

@C.command()
@C.pass_context
def cli_modMSR(ctx):
	"""test  msr kernel module"""
	func.proc.proc_msr()
	
	
entry_point.add_command(read, name="read")
entry_point.add_command(set, name="set")
entry_point.add_command(clear, name="clear")
entry_point.add_command(cli_modMSR, name="msr")

