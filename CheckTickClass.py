#coding: utf8
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUiType

form_class, base_class = loadUiType('UIForms\\checktick.ui')


class CheckTickWindow(QDialog, form_class):
    def __init__(self, *args):
        super(CheckTickWindow, self).__init__(*args)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setupUi(self)

