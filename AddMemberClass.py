#coding: utf8
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUiType
import functions

form_class, base_class = loadUiType('UIForms\\addmember.ui')


class AddMemberWindow(QDialog, form_class):
    def __init__(self, *args):
        super(AddMemberWindow, self).__init__(*args)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setupUi(self)

    def addmembertodb(self):
        clientname = self.lineEdit.text()
        clientage = self.spinBox.value()
        clientexp = self.spinBox_2.value()
        insurnum = self.lineEdit_2.text()
        insurpr = self.lineEdit_3.text()
        insursit = self.lineEdit_4.text()
        ticketnum = self.lineEdit_5.text()
        ticketpr = self.lineEdit_6.text()
        functions.addrowtomember(clientname,clientage,clientexp,insurnum,insurpr,insursit,ticketnum,ticketpr)
        self.close()

