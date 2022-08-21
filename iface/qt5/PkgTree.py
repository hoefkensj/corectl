#!/usr/bin/env python
#   Copyright (c)  2022  Hoefkens J (hoefkensj@gmail.com)
#
from PyQt5 import QtCore, QtGui, QtWidgets
import mod.cpuid.cpuid
import wgtPkgTree
import sys

def create(qtgui,data):
	wgtPkgTree	= QtWidgets.QWidget()
	guiPkgTree	=	qtgui.setupUi(wgtPkgTree)
	
	def popPkgTree(wgt, data):
		def init_cores():
			coreItems = {}
			for core in data['cores'].keys():
				coreItems[core] = QtWidgets.QTreeWidgetItem()
				coreItems[core].setData(0, 0, f'Core {core}')
			return coreItems
		
		pkg = QtWidgets.QTreeWidgetItem()
		pkg.setData(0, 0, data['cpu']['temp']['package']['label']['value'])
		cores = init_cores()
		for core in cores.keys():
			pkg.addChild(cores[core])
		wgt.addTopLevelItem(pkg)


	return guiPkgTree

	

def update(wgt,cpu) :
	fn_freq = cpu['fn']['freq']
	fn_temp = cpu['fn']['temp']
	value_pkgfreq 	= sum([int(fn_freq[c]()) for c in cpu['cores'].keys()])/len(fn_freq.keys())
	print(value_pkgfreq)
	value_pkgtemp		=	int(cpu['cpu']["temp"]["package"]["input"]["rtval"]())
	pkg=wgt.topLevelItem(0)
	pkg.setData(1,0,value_pkgfreq)
	pkg.setData(2,0,value_pkgtemp)
		
		
		#
		# ui.tblCores.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{value_pkgfreq:0.2f}'))
		# ui.tblCores.setItem(0, 2, QtWidgets.QTableWidgetItem(f'  {value_pkgtemp:0.0f}  '))
		
		# 	ui.tblCores.setItem(c+1, 1, QtWidgets.QTableWidgetItem(f'{value_freq:0.2f}'))
		# 	ui.tblCores.setItem(c+1, 2, QtWidgets.QTableWidgetItem(f'  {(value_temp/1000):0.0f}  '))
		# 	# chkBoxItem = ui.tblCores.horizontalHeader.setCheckState(QtCore.Qt.CheckState.Checked)
		# 	# if ui.tblCores.verticalHeaderItem(0).checkState():
		# 	# 	chkBoxItem.setCheckState(QtCore.Qt.CheckState.Checked)
		# 	# else:
		# 	# chkBoxItem.setCheckState(QtCore.Qt.CheckState.Unchecked)
		# 	# PyQt.QtWidgets.QTableWidgetItem.setCheckState(state)
		# 	# ui.tblCores.setItem(c+1, 0, QtWidgets.QTableWidgetItem(chkBoxItem))
		# ui.tblCores.resizeColumnToContents(1)
		# ui.tblCores.resizeColumnToContents(2)

def ui_tmr(ui):
	import types
	def period():
		pass

	def start():return tmr.start(period())
	ns = types.SimpleNamespace()
	tmr = QtCore.QTimer()
	ns.time = start
	ns.run = tmr.timeout.connect
	return ns


def main():
	cpu = mod.cpuid.cpuid.cpu()
	
	win = QtWidgets.QApplication(sys.argv)
	
	QtGui = wgtPkgTree.Ui_wgtPkgTree()
	uiPkgTree=create(QtGui,cpu)
	
	nproc = len(cpu['cores'].keys())

	update(wgt,cpu)

	# gui.spnUpdatePeriod.setDecimals(0)
	# gui.spnUpdatePeriod.setSingleStep(0.1)
	
	upd = update(wgt=gui, cpu=cpu)
	# shwrows = showrows(ui=gui)
	
	tmr = ui_tmr(gui)
	tmr.run(upd)
	tmr.time()
	___ = gui.spnUpdatePeriod.valueChanged.connect(tmr.time)
	# ___		= gui.wtr_Pkg.clicked['QModelIndex'].connect(shwrows)
	___ = wgt.show()
	
	sys.exit(win.exec())




def main2():
	cpu = mod.cpuid.cpuid.cpu()
	
	app = QtWidgets.QApplication(sys.argv)
	
	PkgTree = QtWidgets.QWidget()
	ui = wgtPkgTree.Ui_wgtPkgTree()
	ui.setupUi(PkgTree)

	
	PkgTree.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main2()