#!/usr/bin/env python
import sys
import PyQt6 as PyQt
import tblCores

def read(file): 
	with open(file, 'r') as f:
		c = f.readlines()
	return c[0]*(2>len(c)) +	c[0]*(len(c)>1)


def socket() -> dict :
	import mod.cpuid.cpuid
	def cpuid():
		return mod.cpuid.cpuid.socket()
	return cpuid
	
def Tfrq(**k) -> int :  
	p=k['path'] ; w=k['pow10']
	return (int(read(p))/pow(10,w))

def Ttmps() -> dict :
	import psutil
	import re
	tmps=psutil.sensors_tempergatures()
	cores={}
	rx=re.compile('(^Core (?P<n>\d+)$)')
	c = { 
				0 : [0,1],
				1 : [2,3],
				2 : [4,5],
				3 : [6,7]
			}
		
	for temp in tmps['coretemp']:
		n=rx.search(temp.label)
		if n and n.group('n'):
			cores[c[int(n.group('n'))][0]]=temp.current
			cores[c[int(n.group('n'))][1]]=temp.current
		else :
			cores['S0'] = temp.current
	return cores
		
		


def create(**k) :
	nproc = k['nproc']
	form = k['form']
	
	ui = tblCores.Ui_Form()
	ui.setupUi(form)
	ui.tblCores.setRowCount(nproc+1)
	ui.tblCores.setColumnCount(3)
	ui.tblCores.setHorizontalHeaderLabels(['', 'Frq(MHz)', 'Tmp', ''])
	ui.tblCores.setVerticalHeaderLabels([f'{i}' for i in range(nproc)])
	ui.tblCores.horizontalHeader().stretchLastSection()
	
	for idx in range(nproc):
		chkBoxItem = PyQt.QtWidgets.QTableWidgetItem()
		chkBoxItem.setCheckState(PyQt.QtCore.CheckState)
		ui.tblCores.setItem(idx, 0, PyQt.QtWidgets.QTableWidgetItem(chkBoxItem))
		
		ui.tblCores.setRowHeight(idx, 18)
		ui.tblCores.resizeColumnToContents(0)
		ui.tblCores.resizeColumnToContents(1)
	return ui



def update(**k) : 
	ui = k['ui']
	cores = k['cores']
	def uiupd():
		keysc = cores.keys()
		lstp= [ cores[c]['cpufreq']['scaling_cur_freq']['path'] for c in keysc]
		tmps=Ttmps()
		for idx,p  in enumerate(lstp):
			ui.tblCores.setItem(idx, 1, PyQt.QtWidgets.QTableWidgetItem(f'{Tfrq(path=p,pow10=3):0.2f}'))
			ui.tblCores.setItem(idx, 2, PyQt.QtWidgets.QTableWidgetItem(f'{tmps[idx]:0.0f}\u00B0C'))
		ui.tblCores.resizeColumnToContents(1)
		ui.tblCores.resizeColumnToContents(2)
		return ui
	return uiupd


def main():
	s0 		= socket()
	cpu		= s0()
	win		= PyQt.QtWidgets.QApplication(sys.argv)
	wgt 	= PyQt.QtWidgets.QWidget()
	cores = cpu['cpu']['cores']
	nproc = len(cores.keys())

	gui 	= create(nproc=nproc,form=wgt)
	upd 	= update(ui=gui,cores=cores)
	tmr 	= PyQt.QtCore.QTimer()
	___		=	tmr.timeout.connect(upd)
	___		=	tmr.start(500)
	___		=	wgt.show()

	sys.exit(win.exec())

if __name__ == '__main__':
    main()
