#coding: utf8
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUiType
import functions
form_class, base_class = loadUiType('UIForms\\addfood.ui')


class AddFoodWindow(QDialog, form_class):
    def __init__(self, *args):
        super(AddFoodWindow, self).__init__(*args)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setupUi(self)

    def addfoodtodb(self):
        foodname= self.lineEdit.text()
        number = self.spinBox.value()
        functions.addrowtofood(foodname, number)
        self.close()