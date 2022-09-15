import sys
from PyQt5 import QtWidgets,QtCore,QtGui
import qtdictfb
import types



def make_tree(gui, branches=[], **k):
	def make_branch(root, dct, path):
		for key in dct.keys():
			data = dct[key]
			dictpath = f"{path}['{key}']"
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

def construct_Qt5Ui():
	def QtApp():
		app = types.SimpleNamespace()
		app.QtWin = QtWidgets.QApplication(sys.argv)
		app.QtClip = app.QtWin.clipboard()
		return app

	def Wgt(n=None, t='h'):
		def create():
			nwgt_wgt = QtWidgets.QWidget()
			if t == 'h':
				nwgt_lay = QtWidgets.QHBoxLayout(nwgt_wgt)
			elif t == 'v':
				nwgt_lay = QtWidgets.QVBoxLayout(nwgt_wgt)
			return nwgt_wgt, nwgt_lay
		def init(nwgt_wgt, nwgt_lay):
			nwgt_wgt.setObjectName(f'wgt{n}')
			nwgt_lay.setObjectName(f'lay{n}')
			nwgt_wgt.setContentsMargins(0, 0, 0, 0)
			nwgt_lay.setContentsMargins(0, 0, 0, 0)
			nwgt_lay.setSpacing(0)
			return nwgt_wgt, nwgt_lay
		# def ns(nwgt):
		# 	nwgt.add = nwgt.lay.addWidget
		# 	nwgt.app = nwgt.lay.addItem
		# 	nwgt.width= nwgt.wgt.width
		# 	return nwgt
		qtwgt_wgt, qtwgt_lay = create()
		qtwgt_wgt, qtwgt_lay = init(qtwgt_wgt, qtwgt_lay)
		return qtwgt_wgt, qtwgt_lay

	def make_icon(name, set='Fluent'):
		icon = QtGui.QIcon()
		lset = f'/home/hoefkens/.local/share/icons/{set}/symbolic/actions/{name}.svg'
		dset = f'/home/hoefkens/.local/share/icons/{set}-dark/symbolic/actions/{name}.svg'
		icon.addPixmap(QtGui.QPixmap(dset), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon.addPixmap(QtGui.QPixmap(lset), QtGui.QIcon.Normal, QtGui.QIcon.On)
		return icon
	def iBtn(n, bi=False, h=20, w=20):
		icon = make_icon(n)
		btn = QtWidgets.QToolButton()
		btn.setObjectName(f'tBtn{n}')
		btn.setIcon(icon)
		btn.setIconSize(QtCore.QSize(32, 32))
		btn.setMaximumSize(QtCore.QSize(w, h))
		btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
		btn.setCheckable(bi)
		return btn
	def pBtn(n, bi=False):
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
		btn = QtWidgets.QToolButton()
		btn.setObjectName(f'ibtn{n}')
		btn.setSizePolicy(sizePolicy)
		btn.setText(n)
		btn.setCheckable(bi)
		return btn

	def make_wgtMainCtl():
		spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		def fileCtl():
			btnPrint = pBtn('Print')
			btnSave = pBtn('Save As')
			hWgt_wgt,hWgt_lay = Wgt(t='h')
			hWgt_lay.addWidget(btnPrint)
			hWgt_lay.addWidget(btnSave)
			return hWgt_wgt,hWgt_lay

		def appCtl():
			btnExit = pBtn('Exit')
			hWgt_wgt,hWgt_lay = Wgt(t='h')
			hWgt_lay.addItem(spacerItem)
			hWgt_lay.addWidget(btnExit)
			return hWgt_wgt,hWgt_lay

		filectl_wgt, filectl_lay=fileCtl()
		appctl_wgt, appctl_lay=appCtl()
		hWgt_wgt,hWgt_lay = Wgt(t='h')
		hWgt_lay.addWidget(filectl_wgt)
		hWgt_lay.addWidget(appctl_wgt)
		return hWgt_wgt,hWgt_lay


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
				txtbox.setText(data[0].text(idx))
		return fill
	
	def fitt(gui):
		gui.trDict.expandAll()
		gui.trDict.resizeColumnToContents(0)
		w = gui.trDict.columnWidth(0)
		gui.trDict.setColumnWidth(0, w + 20)
		
		gui.trDict.resizeColumnToContents(1)
		w = gui.trDict.columnWidth(1)
		gui.trDict.setColumnWidth(1, w + 20)
		gui.trDict.collapseAll()
	def copytoclip(txt):
		def toclip():
			App.QtClip.setText(txt.text())
		return toclip
	def editkey(gui):
		def edit(state):
			gui.btnEditKey.setChecked(state)
			gui.txtKey.setReadOnly(not state)
		return edit
	def editval(gui):
		def edit(state):
			gui.btnEditVal.setChecked(state)
			gui.txtVal.setReadOnly(not state)
		return edit
	
	
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
			gui.btnEditKey.setCheckable(True)
			gui.btnEditKey.setChecked(False)
			
		def connect():
			gui.chkSearch.stateChanged.connect(disp(gui.frmSearch))
			gui.chkData.stateChanged.connect(disp(gui.frmData))
			gui.trDict.itemClicked.connect(select(gui))
			gui.btnExp.clicked.connect(gui.trDict.expandAll)
			gui.btnCollapse.clicked.connect(gui.trDict.collapseAll)
			gui.btnCopy.clicked.connect(copytoclip(gui.txtPath))
			# gui.btnSearch.clicked.connect(copyto)
			# gui.btnAbout.clicked.connect(copytoclip)
			gui.btnEditKey.clicked.connect(editkey(gui))
			gui.btnEditVal.clicked.connect(print)
			gui.btnExit.clicked.connect(sys.exit)
			
		gui = qtdictfb.Ui_wgtQtpyDictator()
		gui.setupUi(wgt)
		MainCtl_wgt,MainCtl_lay=make_wgtMainCtl()
		gui.verticalLayout_5.addWidget(MainCtl_wgt)
		init()
		connect()
		
		return gui
	App = QtApp()
	App.Qt5Wgt = QtWidgets.QWidget()
	App.Ui=create(App.Qt5Wgt)
	App.Disp  = disp
	App.Select = select
	App.Fitt = fitt
	App.Create= create
	return App

def browse(**k):
	QtApp = construct_Qt5Ui()
	kv=k.popitem()
	trunk=make_tree(QtApp.Ui, name=kv[0], data=kv[1])

	QtApp.Ui.trDict.addTopLevelItem(trunk)
	QtApp.Fitt(QtApp.Ui)
	QtApp.Qt5Wgt.show()
	sys.exit(QtApp.QtWin.exec())



if __name__ == '__main__' :
	dct = {
		'a' : {
						'aa' : 'aa',
						'ab'  : 'ab'
		},
		'b'  : { 'ba' : 'ba',
              'bb': 'bb'
		}}
	browse(test=dct)
