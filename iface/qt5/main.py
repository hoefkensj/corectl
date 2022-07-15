#!/usr/bin/env python3
import PyQt5
import sys
import iface.qt5.Main
import psutil

def socket():
	import mod.cpuid.cpuid
	
	socket0 = mod.cpuid.cpuid.socket0()
	return socket0
	

class MainWindow(PyQt5.QtWidgets.QMainWindow):

	def __init__(self,*a,**k):
		super(MainWindow, self).__init__(*a,**k)
		# PyQt5.
		# loadUi('Main.ui', self)
		# self.show()
		self.ui = iface.qt5.Main.Ui_MainWindow()
		self.ui.setupUi(self)
	

	socket0=socket()
	
	def update(self):
		socket0 = self.socket0
		cores = socket0['cpu']['cores'].keys()
		for idx, core in enumerate(cores):
			cfrq_ghz(socket0,core)
	
	def msr(self):
		import func.msr
		BD_PROCHOT= func.msr.read_flag(flag='BD_PROCHOT')
		self.ui.ckbBDPROCHOT.setChecked(bool(BD_PROCHOT))
		
	def cmbMng(self):
		socket0=self.socket0
		mng={
					'govs'  : socket0['cpu']['cores']['cpu0']['cpufreq']['scaling_available_governors']['value'],
					'nrgs'  :	socket0['cpu']['cores']['cpu0']['cpufreq']['energy_performance_available_preferences']['value']
			}
		self.ui.cmbGov.clear()
		self.ui.cmbNrg.clear()
		for governor in mng['govs']:
			self.ui.cmbGov.addItem(governor)
		for energy in mng['nrgs']:
			self.ui.cmbNrg.addItem(energy)
	
	def tblCores(self):
		from PyQt5.QtWidgets import QTableWidgetItem,QVBoxLayout,QCheckBox,QHeaderView
		socket0=self.socket0
		cores = socket0['cpu']['cores'].keys()
		self.ui.tblCores.setRowCount(len(cores))
		self.ui.tblCores.horizontalHeader().stretchLastSection()

		for idx,core in enumerate(cores):
			chkBoxItem = QTableWidgetItem()
			chkBoxItem.setCheckState(False)
			frq_cur=socket0['cpu']['cores'][core]['cpufreq']['scaling_cur_freq']['value']
			
			self.ui.tblCores.setItem(idx, 0, QTableWidgetItem(f'Core{idx}'))
			self.ui.tblCores.setItem(idx, 1, QTableWidgetItem(chkBoxItem))
			self.ui.tblCores.setItem(idx, 2, QTableWidgetItem(f'{(int(frq_cur[0])/1000000):0.2f}GHz'))
		self.ui.tblCores.resizeColumnToContents(0)
		self.ui.tblCores.resizeColumnToContents(1)
		self.ui.tblCores.resizeColumnToContents(2)


		# self.sel_governor.setCurrentIndex(self.sel_governor.findText(cpu_get.governor(self.cpu)))
		# self.sel_governor.currentIndexChanged.connect(self.set_governor)
 
	# def tblCores(self):
	# 	self.ui.tblCores.setItem(0,0,'name')
		
		# QTableWidgetItem("Name"))


def cfrq_ghz(socket,core):
	
	frq_hz = socket0['cpu']['cores'][core]['cpufreq']['scaling_cur_freq']['path']

def run():
	Qt5_app = PyQt5.QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.cmbMng()
	window.tblCores()
	window.msr()
	window.show()
	Qt5_app.exec()

if __name__ == "__main__":
	run()
	