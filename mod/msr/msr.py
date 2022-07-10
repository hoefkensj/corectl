#!/usr/bin/env python3
import subprocess
import shlex
import functools
import textwrap


PROC_run	=		functools.partial(  subprocess.run							,
                                  capture_output			=	True	,
                                  universal_newlines	=	True	,	)
S2BIN			=		functools.partial(  int	,	base=2	, )

def load_module() ->int :
	proc=subprocess.run(  ['modprobe' ,'-vvv', 'intel_rapl_msr']					,
                          capture_output			=	True	,
                        )
	return	int(proc.returncode)

def read_0x(addr) -> str:
	command=shlex.split(f'rdmsr -X0 {addr}')
	return PROC_run(command).stdout.strip()

def read_0b(addr) -> str:
	nbits	= len(read_0x(addr))*4
	reads	=	[shlex.split( f'rdmsr --bitfield {i}:{i} {addr}') for i in range(64)]
	bits	= [PROC_run(r).stdout.strip() for r in reads][::-1]
	return str().join(bits)

def read_flag(addr, bit) -> bool:
	command = shlex.split(f'rdmsr --bitfield {bit}:{bit} {addr}')
	return S2BIN(PROC_run(command).stdout.strip())

def read_BDPROCHOT() -> bool:
	BD_PROCHOT = read_flag(0x1FC, 0)
	return bool(BD_PROCHOT)

def write_0x(reg,val)	-> str:
	command=shlex.split(f'wrmsr -a {reg} 0x{val}')
	return PROC_run(command).stdout.strip()

def write_flag(addr,bit, val) ->str:
	value=str(val)
	str_regog				=		read_0b(addr)
	lst_regog				=		textwrap.wrap(str_regog,1)
	lst_rregog			=   lst_regog[::-1]
	lst_rregnw			=		lst_rregog
	lst_rregnw[bit]	=		value
	lst_regnw				=   lst_rregnw[::-1]
	str_regnw				=		str().join(lst_regnw)
	x_value					=		f'{S2BIN(str_regnw):x}'
	result					=		write_0x(addr, x_value)
	return result

def write_BDPROCHOT(val) -> str:
		result				= write_flag(0x1FC, 0, val)
		return



