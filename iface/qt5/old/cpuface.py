"""
    This module shows the CPU Face UI
    And add specific function
"""

#

  

#
#

#
#

#
#







from PyQt5.QtWidgets import QDialog, QMessageBox, QInputDialog,QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
from os import path



class Cpuface(QMainWindow):

	def __init__(self):
		super(Cpuface, self).__init__()
		data = path.dirname(__file__)
		loadUi('Main.ui', self)
		self.show()





    def update_ui(self):
        # Disable all unwanted calls
        try:
            self.sel_profile.currentIndexChanged.disconnect()
            self.sel_cpu.currentIndexChanged.disconnect()
            self.check_online.stateChanged.disconnect()
            self.sel_governor.currentIndexChanged.disconnect()
            self.val_speed.valueChanged.disconnect()
            self.btn_new.clicked.disconnect()
            self.btn_save.clicked.disconnect()
            self.btn_remove.clicked.disconnect()
        except TypeError:
            pass

        # Disable all options
        self.sel_profile.setEnabled(False)
        self.sel_cpu.setEnabled(False)
        self.check_online.setEnabled(False)
        self.sel_governor.setEnabled(False)
        self.val_speed.setEnabled(False)
        self.btn_new.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.btn_remove.setEnabled(False)

        # Update profile selection
        prof_index = self.sel_profile.currentIndex()
        if prof_index == -1:
            prof_index = 0
        self.sel_profile.clear()
        self.sel_profile.addItem("No profile")
        for profile in self.profiles:
            self.sel_profile.addItem(profile)
        self.sel_profile.setCurrentIndex(prof_index)
        self.sel_profile.currentIndexChanged.connect(self.set_profile)
        self.sel_profile.setEnabled(True)

        # Update CPU selection
       
        self.cpu = self.sel_cpu.currentIndex()
        if self.cpu == -1:
            self.cpu = 0
        self.sel_cpu.clear()
        for i, cpu in enumerate(self.cpuinfo):
            self.sel_cpu.addItem("CPU %d: %s" % (i, cpu["name"]))
        self.sel_cpu.setCurrentIndex(self.cpu)
        self.sel_cpu.currentIndexChanged.connect(self.update_ui)
        self.sel_cpu.setEnabled(True)

        # Update current CPU status


        # Update current CPU governor
        self.sel_governor.clear()



        self.sel_governor.currentIndexChanged.connect(self.set_governor)


        # Update current speed


        self.val_speed.valueChanged.connect(self.set_speed)


        # Update additional information
        self.lab_driver.setText(self.cpuinfo[self.cpu]["driver"])
        self.lab_vendor.setText(self.cpuinfo[self.cpu]["vendor"])
        self.lab_cpu_id.setText(self.cpuinfo[self.cpu]["id"])
        self.lab_core_id.setText(self.cpuinfo[self.cpu]["core"])
        self.lab_cache.setText(str(self.cpuinfo[self.cpu]["cache"]))

        # Update buttons action
        self.btn_new.clicked.connect(self.new_profile)
        self.btn_new.setEnabled(True)
        if self.sel_profile.currentText() != "No profile":
            self.btn_save.clicked.connect(self.save_profile)
            self.btn_save.setEnabled(True)
            self.btn_remove.clicked.connect(self.remove_profile)
            self.btn_remove.setEnabled(True)

    def detect_error(self, result):
        if result[0] != 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Unable to update CPU Status\n\nError Code: %d" % result[0])
            msg.setDetailedText(result[1])
            msg.setWindowTitle("Unable to update CPU Status")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec_()

    def set_online(self):

        self.update_ui()

    def set_governor(self):

        self.update_ui()

    def set_speed(self):

        self.update_ui()

    def new_profile(self):
        input_name = QInputDialog(self)
        input_name.setLabelText("Profile Name")
        input_name.setOkButtonText("Create")
        input_name.exec_()
        name = input_name.textValue()

        if name != '':
            self.save_profile(name)

    def save_profile(self, name=None):
        if type(name) is bool or name is None:
            name = self.sel_profile.currentText()



    def remove_profile(self):
        del self.profiles[self.sel_profile.currentText()]
        self.update_ui()
        self.sel_profile.setCurrentIndex(0)

    def set_profile(self):
        if self.sel_profile.currentIndex() > 0:
            profile = self.sel_profile.currentText()

        self.update_ui()
