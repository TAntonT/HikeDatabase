#coding: utf8
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUiType
import functions


form_class, base_class = loadUiType('UIForms\\addroute.ui')


class AddRouteWindow(QDialog, form_class):
    def __init__(self, *args):
        super(AddRouteWindow, self).__init__(*args)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setupUi(self)

    def addroutetodb(self):
        routename= self.lineEdit_2.text()
        country = self.lineEdit.text()
        price = self.lineEdit_3.text()
        distance = self.spinBox.value()
        difficult = self.comboBox.currentText()
        if not self.checkBox.isChecked() == True:
            oxygen = 0
        else:
            oxygen = 1
        functions.addrowtoroutes(routename, country, difficult, oxygen, distance)
        functions.addfirm_to_rote(price)
        self.close()