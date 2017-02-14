#coding: utf8
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUiType
import functions

form_class, base_class = loadUiType('UIForms\\addfirm.ui')


class AddFirmWindow(QDialog, form_class):
    def __init__(self, *args):
        super(AddFirmWindow, self).__init__(*args)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setupUi(self)

    def addfirmtodb(self):
        firmname = self.lineEdit.text()
        firmscore = self.spinBox.value()
        functions.addrowtofirms(firmname, firmscore)
        self.close()
