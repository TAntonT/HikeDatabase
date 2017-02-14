#coding: utf8
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUiType
import functions

form_class, base_class = loadUiType('UIForms\\addguide.ui')


class AddGuideWindow(QDialog, form_class):
    def __init__(self, *args):
        super(AddGuideWindow, self).__init__(*args)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setupUi(self)

    def addguidetodb(self):
        name = self.lineEdit.text()
        age = self.spinBox.value()
        exp = self.spinBox_2.value()
        functions.addrowtoguide(name,exp, age)
        self.close()
