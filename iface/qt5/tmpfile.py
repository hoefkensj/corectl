


#
#  set ( $len = $NAME.length() - 3 )
#  set ( $fileName = $NAME.substring(0, $len) )
#   Copyright (c)  2022  Hoefkens J (hoefkensj@gmail.com)
#

#!/usr/bin/env python
# Auth
#!/usr/bin/env python



import sys
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import frmPkgCores
# import frmPkgCores
import mod.cpuid.cpuid
import types




def create(trdata):
	def size(wgt):
		pols = {
			'mExp': QtWidgets.QSizePolicy.MinimumExpanding
			}
		pol = QtWidgets.QSizePolicy(pols['mExp'], pols['mExp'])
		pol.setHorizontalStretch(0)
		pol.setVerticalStretch(0)
		wgt.setSizePolicy(pol)
		return wgt
	def markup(wgt):
		wgt.setContentsMargins(0, 0, 0, 0)
		return wgt
	def populate(wgt, data):
		def init_cores():
			coreItems = {}
			for core in data['cores'].keys():
				coreItems[core] = QtWidgets.QTreeWidgetItem()
				coreItems[core].setData(0, 0, f'Core {core}')
			return coreItems
		wgt.setColumnCount(3)
		pkg = QtWidgets.QTreeWidgetItem()
		pkg.setData(0, 0, data['cpu']['temp']['package']['label']['value'])
		cores = init_cores()
		for core in cores.keys():
			pkg.addChild(cores[core])
		wgt.addTopLevelItem(pkg)
		print(dir(wgt))
		return wgt
	wrap_WTrCpu = QtWidgets.QWidget()
	wrap_WTrCpu.setObjectName('wrap_WTrCpu')
	wrap_WTrCpu=size(markup(wrap_WTrCpu))
	vLay1 = QtWidgets.QVBoxLayout(wrap_WTrCpu)
	vLay1.setObjectName('vLay1')
	# vLay1 = markup(vLay1)
	WTr_cpu = QtWidgets.QTreeWidget()
	WTr_cpu.setObjectName('WTr_cpu')
	WTr_cpu=size(markup(WTr_cpu))
	WTr_cpu=populate(WTr_cpu,trdata)
	vLay1.addWidget(WTr_cpu)
	return wrap_WTrCpu




def update(wgt,data):
	pkg0=wgt.vLay1
	for child in pkg0:
		freq=int(data['cores'][child]["cpufreq"]["scaling_cur_freq"]["rtval"]())
		pkg0.child(child).setData(1,0,f'{freq}')

	
		
	
	# def update_freqs():
	# 			freqs=[]
	#
	# 				freq=int(data['cores'][core]["cpufreq"]["scaling_cur_freq"]["rtval"]())
	# 				freqs+=[freq]
	# 				coreItem=QtWidgets.QTreeWidgetItem()
	#
	#
	# 				subitems+=[						QtWidgets.QTreeWidgetItem(							[ f'Core {core}' ,								f'{freq}',
	# 							data['cores'][core]['hwmon']['coretemp']['parameters']['input']['rtval'](), ])			 ]
	# 			pkgfreq=int(sum(freqs)/len(freqs))
	# 			item = QtWidgets.QTreeWidgetItem([
	# 				,
	# 				f'{pkgfreq}',
	# 				data['cpu']['temp']['package']['input']['rtval'](), 'd'])
	# 				print(item.setData(2,0,10))
	# 				for subitem in subitems:
	# 					item.addChild(subitem)
		



	
	
	
	


win = QtWidgets.QApplication(sys.argv)
cpu=mod.cpuid.cpuid.cpu()
# value_pkgfreq = avrg([float(cpu["cores"][c]["cpufreq"]["scaling_cur_freq"]["rtval"]())/1000 for c in cpu['cores'].keys()])
# value_pkgtemp=int(cpu['cpu']["temp"]["package"]["input"]["rtval"]())/1000
ui=create(cpu)
ui=update(ui,cpu)
[print(item) for item in dir(ui)]
___		=	ui.show()


sys.exit(win.exec())
