#coding: utf8
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUiType
import functions

form_class, base_class = loadUiType('UIForms\\addhike.ui')


class AddHikeWindow(QDialog, form_class):
    def __init__(self, *args):
        super(AddHikeWindow, self).__init__(*args)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setupUi(self)

    def addcomboboxitems(self):
        t=functions.changecmbbox()
        self.comboBox_3.clear()
        self.comboBox_3.addItems(t[0])
        self.comboBox_2.clear()
        self.comboBox_2.addItems(t[1])

    def addhiketodb(self):
        routename= self.comboBox_2.currentText()
        firmname = self.comboBox_3.currentText()
        datestart = str(self.dateEdit.date().toString("dd.MM.yy"))
        dateend = str(self.dateEdit_2.date().toString("dd.MM.yy"))
        transport = self.comboBox_5.currentText()
        functions.addrowtohike(firmname, routename, datestart, dateend, transport)
        self.close()
