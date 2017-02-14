#coding: utf8
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUiType
import functions

form_class, base_class = loadUiType('UIForms\\addequipment.ui')


class AddEquipmentWindow(QDialog, form_class):
    def __init__(self, *args):
        super(AddEquipmentWindow, self).__init__(*args)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setupUi(self)

    def addequipmenttodb(self):
        type= self.comboBox.currentText()
        weight = self.comboBox_2.currentText()
        properties = self.comboBox_3.currentText()
        code = self.lineEdit.text()
        functions.addrowtoequipment(type, weight, properties, code)
        self.close()