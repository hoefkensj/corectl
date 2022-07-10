#!/usr/bin/env python3
import PyQt5
import sys
import Main
import psutil
import

class MainWindow(PyQt5.QtWidgets.QMainWindow):

	def __init__(self,*a,**k):
		super(MainWindow, self).__init__(*a,**k)
		# PyQt5.
		# loadUi('Main.ui', self)
		# self.show()
		self.ui = Main.Ui_MainWindow()
		self.ui.setupUi(self)
	
	def cmbGov(self):
		self.ui.cmbGov.clear()
		for governor in ):
			self.sel_governor.addItem(governor)
		self.sel_governor.setCurrentIndex(self.sel_governor.findText(cpu_get.governor(self.cpu)))
		self.sel_governor.currentIndexChanged.connect(self.set_governor)
 
	# def tblCores(self):
	# 	self.ui.tblCores.setItem(0,0,'name')
		
		# QTableWidgetItem("Name"))


def Govs():




if __name__ == "__main__":
	Qt5_app = PyQt5.QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.tblCores()
	window.show()
	Qt5_app.exec()
	