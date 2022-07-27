#!/usr/bin/env python



import sys
import PyQt5 as PyQt
import frm_tblPkgCores
import mod.cpuid.cpuid
import types

def read(file): 
	with open(file, 'r') as f:
		c = f.readlines()
	return c[0]*(2>len(c)) +	c[0]*(len(c)>1)

def read_sysfs(path):
	with open(path) as f:
		c=f.readline().strip()
	return c


def Tfrq(**k) -> int :  
	p=k['path'] ; w=k['pow10']
	return (int(read(p))/pow(10,w))

def Ttmps() -> dict :
	import psutil
	import re
	tmps=psutil.sensors_temperatures()
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
		
		


def create(nproc,form) :
	def Pkg():
		ui= frm_tblPkgCores.Ui
		ui.tblCores.setRowCount(nproc)
		ui.tblCores.setColumnCount(3)
		ui.tblCores.setHorizontalHeaderLabels(['', 'Frq(MHz)', 'Tmp', ''])
		ui.tblCores.setVerticalHeaderLabels([f'{i}' for i in range(nproc)])
		ui.tblCores.horizontalHeader().stretchLastSection()
		return ui
	
	def Cores():
		ui = frm_tblPkgCores.Ui_Form()
		ui.setupUi(form)
		ui.tblCores.setRowCount(nproc)
		ui.tblCores.setColumnCount(3)
		ui.tblCores.setHorizontalHeaderLabels(['', 'Frq(MHz)', 'Tmp', ''])
		ui.tblCores.setVerticalHeaderLabels([f'{i}' for i in range(nproc)])
		ui.tblCores.horizontalHeader().stretchLastSection()
		for idx in range(nproc):
			chkBoxItem = PyQt.QtWidgets.QTableWidgetItem()
			chkBoxItem.setCheckState(PyQt.QtCore.Qt.CheckState.Checked)
			# PyQt.QtWidgets.QTableWidgetItem.setCheckState(state)
			ui.tblCores.setItem(idx, 0, PyQt.QtWidgets.QTableWidgetItem(chkBoxItem))
			
			ui.tblCores.setRowHeight(idx, 18)
			ui.tblCores.resizeColumnToContents(0)
			ui.tblCores.resizeColumnToContents(1)
		return ui
	
	
	ui=Cores()
	return ui



def update(ui,cores) :
	def ui_upd():
		keysc = cores.keys()
		lstp= [ cores[c]['cpufreq']['scaling_cur_freq']['path'] for c in keysc]
		tmps=Ttmps()
		for idx,p  in enumerate(lstp):
			ui.tblCores.setItem(idx, 1, PyQt.QtWidgets.QTableWidgetItem(f'{Tfrq(path=p,pow10=3):0.2f}'))
			ui.tblCores.setItem(idx, 2, PyQt.QtWidgets.QTableWidgetItem(f'{tmps[idx]:0.0f}\u00B0C'))
		ui.tblCores.resizeColumnToContents(1)
		ui.tblCores.resizeColumnToContents(2)
		return ui
	return ui_upd

def ui_tmr(ui):
	def period():return int(float(ui.spnUpdatePeriod.value()) * 1000)
	def start():return tmr.start(period())
	ns = types.SimpleNamespace()
	tmr = PyQt.QtCore.QTimer()
	ns.time = start
	ns.run = tmr.timeout.connect
	return ns
	
def main():
	cpu		= mod.cpuid.cpuid.cpu()
	win		= PyQt.QtWidgets.QApplication(sys.argv)
	wgt 	= PyQt.QtWidgets.QWidget()
	cores = cpu['cores']
	nproc = len(cores.keys())

	gui 	= create(nproc=nproc,form=wgt)
	upd 	= update(ui=gui,cores=cores)



	tmr 	= ui_tmr(gui)
	tmr.run(upd)
	tmr.time()
	#PyQt.QtCore.QTimer()
	# ___		= tmr.start(500)
	___ 	=	gui.spnUpdatePeriod.valueChanged.connect(tmr.time)
	# ___		=	tmr.timeout.connect(upd)
	
	___		=	wgt.show()

	sys.exit(win.exec())

if __name__ == '__main__':
    main()
