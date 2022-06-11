#!/usr/bin/env python
import click as C
import func.main
import func.proc
import func.msr
import func.stdfn
import static.locale
import func.stdfn
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
def cli_chk(ctx):
	"""Check MSR: 0x1FC[0]"""
	check=func.proc.proc_chk()
	data=[
				['  MSR #0x1FC',check,]
	]
	# std_out=func.stdfn.std_row(check,'MSR #0x1FC' ,2)
	# C.echo([f'{it}\n' for it in std_out])
	stdout_str=itrface.cli.clo.stdout_table(ctx.parent.params['table'])
	C.echo(stdout_str(data).format(placeholderw16=f"{row[1]['HEXX'][:-4]}\x1b[1;32m{row[1]['HEXX'][-4:]}\x1b[0m"))

@C.command()
@C.pass_context
def cli_set(ctx):
	"""Set BD_PROCHOT Flag (set to 1)"""
	out=itrface.cli.clo.stdout_table(ctx)
	check	= func.proc.proc_chk()
  orr,result	= func.proc.proc_set(check)
	std_out=[0,0,0]
	std_out[0]= func.stdfn.std_row(check, 'MSR #0x1FC', 2)
	std_out[1]= func.stdfn.std_row(orr, ' OR #0x1FC', 2)
	std_out[2]= func.stdfn.std_row(result, 'NEW #0x1FC', 2)
	
	C.echo(std_out)
func.msr.wrmsr_0x1FC(result['HEXX'])
	return
	
@C.command()
@C.pass_context
def cli_clr(ctx):
	"""Clear BD_PROCHOT Flag (set to 0)"""
	check	= func.proc.proc_chk()
  andd,result	= functions.proc.proc_clr(check)
	std_out=std_box=[0,0,0]

	# C.echo(table)
  std_out[0],std_box[0] = functions.stdfn.std_row(check, 'MSR #0x1FC', 2)
  std_out[1],std_box[1] = functions.stdfn.std_row(andd, 'AND #0x1FC', 2)
	
  std_out[2],std_box[2] = functions.stdfn.std_row(result, 'NEW #0x1FC', 2)
	
	# table=func.stdfn.dec_boxdraw().format(rows=f'\n{std_box[0]}\n{std_box[1]}\n\n{std_box[2]}\n')
	
	# C.echo(table)
	C.echo(std_out)
	# func.msr.wrmsr_0x1FC(result['HEXX'])
	return

@C.command()
@C.pass_context
def cli_modMSR(ctx):
	"""test  msr kernel module"""
	func.proc.proc_msr()
	
	
entry_point.add_command(cli_chk, name="check")
entry_point.add_command(cli_set, name="set")
entry_point.add_command(cli_clr, name="reset")
entry_point.add_command(cli_modMSR, name="msr")

