#!/usr/bin/env python



import sys
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import frmPkgCores
import mod.cpuid.cpuid
import types
import qt5dictator

def create(nproc,form) :
	ui = frmPkgCores.Ui_Form()
	ui.setupUi(form)

	def table(gui):
		gui.setRowCount(nproc+1)
		gui.setColumnCount(3)
		gui.setHorizontalHeaderLabels(['', 'Frq(MHz)', '\u00B0C  ' , ''])
		font =  QtGui.QFont()
		font.setBold(True)
		gui.setVerticalHeaderLabels(['╰─⊞ Package 0',*[f'      ├╼ Core {i+1}' for i in range(nproc)]])
		gui.verticalHeaderItem(0).setFont(font)
		gui.verticalHeader().setFrameShape(QtWidgets.QFrame.NoFrame)
		gui.verticalHeader().setFrameShadow(QtWidgets.QFrame.Plain)

		# gui.verticalHeader().setFrameRect(QtGui.Q)
		# gui.horizontalHeader().stretchLastSection()
		gui.resizeColumnsToContents()
		gui.resizeRowsToContents()
		gui.horizontalHeader().stretchLastSection()
		gui.horizontalHeader().setVisible(True)
		for idx in range(1,(nproc+1)):
			chkBoxItem = QtWidgets.QTableWidgetItem()
			if gui.verticalHeaderItem(0).checkState():
				chkBoxItem.setCheckState(QtCore.Qt.CheckState.Checked)
			else:
				chkBoxItem.setCheckState(QtCore.Qt.CheckState.Unchecked)
			# PyQt.QtWidgets.QTableWidgetItem.setCheckState(state)
			gui.setItem(idx, 0, QtWidgets.QTableWidgetItem(chkBoxItem))
			gui.setRowHeight(idx, 15)
			gui.resizeColumnToContents(0)
			gui.resizeColumnToContents(1)
			gui.setRowHidden(idx,True)
		return gui
	
	table(form)
	# Cores(ui)

	return ui

def avrg(list):
	return int(sum(list)/len(list))
	

def update(ui,cpu) :
	def ui_upd():
		value_pkgfreq = avrg([float(cpu["cores"][c]["cpufreq"]["scaling_cur_freq"]["rtval"]())/1000 for c in cpu['cores'].keys()])
		value_pkgtemp=int(cpu['cpu']["temp"]["package"]["input"]["rtval"]())/1000
		
		ui.tblCores.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{value_pkgfreq:0.2f}'))
		ui.tblCores.setItem(0, 2, QtWidgets.QTableWidgetItem(f'  {value_pkgtemp:0.0f}  '))
		for c in cpu['cores'].keys():
			value_freq=float(cpu["cores"][c]["cpufreq"]["scaling_cur_freq"]["rtval"]())/1000
			value_temp=float(cpu['cores'][c]['hwmon']['coretemp']['parameters']['input']['rtval']())
			ui.tblCores.setItem(c+1, 1, QtWidgets.QTableWidgetItem(f'{value_freq:0.2f}'))
			ui.tblCores.setItem(c+1, 2, QtWidgets.QTableWidgetItem(f'  {(value_temp/1000):0.0f}  '))
			chkBoxItem = QtWidgets.QTableWidgetItem()
			if ui.tblCores.verticalHeaderItem(0).checkState():
				chkBoxItem.setCheckState(QtCore.Qt.CheckState.Checked)
			else:
				chkBoxItem.setCheckState(QtCore.Qt.CheckState.Unchecked)
			# PyQt.QtWidgets.QTableWidgetItem.setCheckState(state)
			ui.tblCores.setItem(c+1, 0, QtWidgets.QTableWidgetItem(chkBoxItem))
		ui.tblCores.resizeColumnToContents(1)
		ui.tblCores.resizeColumnToContents(2)
		return ui
	return ui_upd

def ui_tmr(ui):
	def period():
		time=float(ui.spnUpdatePeriod.value())
		step=ui.spnUpdatePeriod.singleStep()
		if 0.1 < time <= 1.0 :
			ui.spnUpdatePeriod.setSingleStep(0.1)
			ui.spnUpdatePeriod.setDecimals(1)
		elif 0.01 < time <= 0.10 :
			ui.spnUpdatePeriod.setSingleStep(0.01)
			ui.spnUpdatePeriod.setDecimals(2)
		elif 0.001 < time <= 0.010 :
			ui.spnUpdatePeriod.setSingleStep(0.001)
			ui.spnUpdatePeriod.setDecimals(3)
		elif 0.0001 <= time <= 0.0010 :
			ui.spnUpdatePeriod.setSingleStep(0.0001)
			ui.spnUpdatePeriod.setDecimals(4)
		else :
			ui.spnUpdatePeriod.setSingleStep(1)
		return int(time*1000)
	def start():return tmr.start(period())
	ns = types.SimpleNamespace()
	tmr = QtCore.QTimer()
	ns.time = start
	ns.run = tmr.timeout.connect
	return ns
def showrows(ui):
	def showhide():
		for i in range(1,9):
			state=not ui.tblCores.isRowHidden(i)
			ui.tblCores.setRowHidden(i,state)
	return showhide
def main():
	cpu		= mod.cpuid.cpuid.cpu()
	qt5dictator.browse(cpu=cpu)
	win		= QtWidgets.QApplication(sys.argv)
	wgt 	= QtWidgets.QWidget()
	cores = cpu['cores']
	
	nproc = len(cores.keys())

	gui 	= create(nproc=nproc,form=wgt)
	gui.spnUpdatePeriod.setDecimals(0)
	gui.spnUpdatePeriod.setSingleStep(0.1)
	
	upd 	= update(ui=gui,cpu=cpu)
	shwrows=showrows(ui=gui)



	tmr 	= ui_tmr(gui)
	tmr.run(upd)
	tmr.time()
	___ 	=	gui.spnUpdatePeriod.valueChanged.connect(tmr.time)
	___		= gui.tblCores.clicked['QModelIndex'].connect(shwrows)
	___		=	wgt.show()

	sys.exit(win.exec())

if __name__ == '__main__':
    main()
