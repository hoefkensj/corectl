#!/usr/bin/env python
from ansitable import ANSITable, Column
import types

def layout(style):
	table = ANSITable(
		Column("name", colalign="^"),
		Column("hexx", colalign="^"),
		Column("nibb", colalign="^"),
		header				=	False,
		border 				= style,
		bordercolor 	= "white",
		colsep				= 4,
		offset= 2,
		)
	return table

def populate(table,data):
	for i, row in enumerate(data):
		table.row(row[0], '{'+f'placeholder{}', row[1]['NIBB'])
	return table

def stdout_table(celldata,type='fancy'):
	data=celldata
	worktable=''
	def fancy(data):
		worktable=layout('double')
		print(repr(data))
		for i,row in enumerate(data):
			data[i][1]['NIBB']=["\u2502".join(row[1]['NIBB'][-4:])]

		worktable=populate(worktable,data)
		return worktable
	
	def minimal(data):
		worktable = layout('ascii')
		print(repr(data))
		for i, row in enumerate(data[1]):
			data[i][1]['NIBB'] = ["|".join(row[1]['NIBB'][-3:])]
		worktable = populate(worktable, data)
		return worktable
	
	table=types.SimpleNamespace()
	table.fancy		= fancy
	table.minimal	= minimal
	
	tables={
		'fancy' : table.fancy,
		'minimal': table.minimal,
	}


	return tables[type]


