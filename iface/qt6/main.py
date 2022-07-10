#!/usr/bin/env python
# import PySide6
import sys, os

from PyQt6.QtWidgets import QDialog, QMessageBox, QInputDialog, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6.uic import loadUi

import sys, os
from PyQt6.QtWidgets import QApplication

class MainWindow6(QMainWindow):
	def __init__(self, *a, **k):
		super(MainWindow6, self).__init__(*a, **k)
		loadUi('Main.ui', self)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow6()
	
	quit(app.exec())



