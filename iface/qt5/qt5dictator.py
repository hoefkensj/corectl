import sys
from PyQt5 import QtWidgets
import qtdictfb



def window(*a,**k):
	win = QtWidgets.QApplication(sys.argv)
	def display(gui):
		gui.show()
		sys.exit(win.exec())
	return display

def make_tree(gui, branches=[], **k):
	def make_branch(root, dct, path):
		for key in dct.keys():
			data = dct[key]
			dictpath = f'{path}["{key}"]'
			branch = QtWidgets.QTreeWidgetItem()
			branch.setText(0, str(key))
			branch.setText(2, dictpath)
			if isinstance(data, dict):
				make_branch(branch, data, dictpath)
			else:
				data = str(data)
				w = gui.trDict.columnWidth(1)
				data = repr(data) if callable(data) else data
				dispdata = f'{data[0:w - 4]}...' if len(data) > w - 4 else data
				branch.setText(1, dispdata)
				branch.setText(3, data)
			root.addChild(branch)

	name = k['name']
	data = k['data']
	root = QtWidgets.QTreeWidgetItem()
	root.setText(0, name)
	root.setText(2, name)
	make_branch(root, data, name)
	return root



def construct_Qt5Ui( Qt5Wgt ):

	def disp(gui):
		frm=[gui.hide,'',gui.show]
		def showhide(state):
			frm[state]()
		return showhide
		
	def select(gui):
		txtBox=[ gui.txtKey,gui.txtVal,gui.txtPath,]
		def fill():
			data=gui.trDict.selectedItems()
			for  idx,txtbox in zip( [0,3,2],txtBox):
				txtBox[idx].setText(data[0])
		return fill
	
	def adaptView(gui):
		gui.trDict.resizeColumnToContents(0)
		w = gui.trDict.columnWidth(0)
		gui.trDict.setColumnWidth(0, w + 20)
		
		gui.trDict.resizeColumnToContents(1)
		w = gui.trDict.columnWidth(1)
		gui.trDict.setColumnWidth(1, w + 20)
	
	# def select(gui):
	# 	def show():
	# 		txt = {
	# 			'key' : gui.txtKey,
	# 			'val' : gui.txtVal,
	# 			'path': gui.txtPath,
	# 			}
	# 		selected = gui.trDict.selectedItems()
	# 		adaptView()
	# 		for item in selected:
	# 			txt['key'].setText(str(item.data(0, 0)))
	# 			txt['val'].setText(str(item.data(3, 0)))
	# 			txt['path'].setText(str(item.data(2, 0)))
	# 	return show

	def create(wgt):
		def init():
			gui.trDict.expandAll()
			gui.trDict.resizeColumnToContents(0)
			gui.trDict.resizeColumnToContents(1)
			gui.trDict.collapseAll()
			gui.trDict.expandItem(gui.trDict.topLevelItem(0))
			gui.trDict.setColumnCount(4)
			gui.trDict.hideColumn(2)
			gui.trDict.hideColumn(3)
			gui.frmData.hide()
			gui.frmSearch.hide()

			
		def connect():

			gui.chkSearch.stateChanged.connect(disp(gui.frmSearch))
			gui.chkData.stateChanged.connect(disp(gui.frmData))
			gui.trDict.itemClicked.connect(select(gui))
			gui.btnExp.clicked.connect(gui.trDict.expandAll)
			gui.btnCollapse.clicked.connect(gui.trDict.collapseAll)
			gui.btnCopy.clicked.connect()
			gui.btnSearch.clicked.connect()
			gui.btnAbout.clicked.connect()
			
			
			
			
			gui.btnExit.clicked.connect(sys.exit)
			
			
			
		gui = qtdictfb.Ui_wgtQtpyDictator()
		gui.setupUi(wgt)
		init()
		connect()

		return gui
	ui=create(Qt5Wgt)
	return ui

def browse(**k):

	QtWin = QtWidgets.QApplication(sys.argv)
	QtpyDictator = QtWidgets.QWidget()
	gui = construct_Qt5Ui(QtpyDictator)

	kv=k.popitem()
	trunk=make_tree(gui, name=kv[0], data=kv[1])

	gui.trDict.addTopLevelItem(trunk)

	QtpyDictator.show()
	sys.exit(QtWin.exec())
	
