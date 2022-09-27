#!/usr/bin/env python3

import sys,os

import mod.cpuid.cpuid
from PyQt5 import QtCore, QtGui, QtWidgets
import qtdictfb
import types

def construct_Qt5Ui():
	win = QtWidgets.QApplication(sys.argv)

	
	def create(wgt):
		wgtQtpyDictator = QtWidgets.QWidget()
		gui=qtdictfb.Ui_wgtQtpyDictator.setupUi(wgtQtpyDictator)

		gui = qtdictfb.Ui_wgtQtpyDictator()
		gui.setupUi(wgtQtpyDictator)
		return (win,gui)
	
	def init(gui):
		gui.frmAuto.hide()
		gui.frmState.hide()
		gui.frmSearch.hide()
		gui.trDict.expandAll()
		gui.trDict.resizeColumnToContents(0)
		gui.trDict.resizeColumnToContents(1)
		gui.trDict.collapseAll()
		gui.trDict.expandItem(gui.trDict.topLevelItem(0))
		gui.trDict.setColumnCount(4)
		gui.trDict.hideColumn(2)
		gui.trDict.hideColumn(3)


def maketree(gui,branches=[],**k):
	def makebranches(root, dct, path):
		for key in dct.keys():
			data = dct[key]
			dictpath = f'{path}["{key}"]'
			
			branch = QtWidgets.QTreeWidgetItem()
			branch.setText(0, str(key))
			branch.setText(2, dictpath)
			
			if isinstance(data, dict):
				makebranches(branch, data, dictpath)
			else:
				data = str(data)
				w = gui.trDict.columnWidth(1)
				data = repr(data) if callable(data) else data
				if len(data) > (w - 4):
					dispdata = f'{data[0:(w - 4)]}...'
				else:
					dispdata = data
				branch.setText(1, dispdata)
				branch.setText(3, data)
			root.addChild(branch)
	name=k['name']
	data=k['data']
	root = QtWidgets.QTreeWidgetItem()
	root.setText(0, name)
	root.setText(2, name)
	makebranches(root,data,name)
	return root



def update(gui):
	def update():
		txt = {
			'key'   : gui.txtKey,
			'val'   : gui.txtVal,
			'path'  : gui.txtPath,
			}
		selected = gui.trDict.selectedItems()
		for item in selected:
			txt['key'].setText(str(item.data(0,0)))
			txt['val'].setText(str(item.data(3,0)))
			txt['path'].setText(str(item.data(2,0)))
	return update


def show(gui,frame):
	def showhide():
		frames={
			'State' : [gui.chkState,gui.grpState],
			'Search':	[gui.chkSearch,gui.grpSearch],
			'Auto'  : [gui.chkAuto,gui.grpAuto],}
			
		if frames[frame][0].checkState():
			frames[frame][1].show()
		else:
			frames[frame][1].hide()
	return showhide
	
def connect(gui):
	state= show(gui,'State')
	search = show(gui, 'Search')
	auto= show(gui,'Auto')
	gui.chkState.stateChanged.connect(state)
	gui.chkSearch.stateChanged.connect(search)
	gui.chkAuto.stateChanged.connect(auto)
	gui.trDict.itemClicked.connect(UiUpdate)




def main(**k):
	QtWin=createUi()




	name = str(list(k)[0])
	data=k[name]
	
	
	tree=maketree(ui,name=name,data=data)
	ui.trDict.addTopLevelItem(tree)
	initUi(ui)

	UiUpdate = update(ui)


	wgtQtpyDictator.show()
	sys.exit(win.exec())
	
	
if __name__ == "__main__":
	dct = mod.cpuid.cpuid.cpu()
	main(cpu=dct)