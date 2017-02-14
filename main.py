#coding: utf8
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUiType

import AddHikeClass, AddFoodClass, AddMemberClass, AddEquipmentClass, AddFirmClass, AddGuideClass, AddRouteClass
import CheckInsClass, CheckTickClass
import functions

app = QApplication(sys.argv)
app.setApplicationName('CourseWork1')
form_class, base_class = loadUiType('UIForms\\window.ui')

ind=0 #индикатор клика мышки для редактирования таблицы
ind1=0
ind2=0
ind3=0

#переменные для фирмы
delrow=0 #строка, которую надо удалить
delid=0 #id которое надо удалить

#переменные для маршрута
delrow1=0
delid1=0

#переменные для проводников
delrow2=0
delid2=0

#переменные для походов
delrow3=0
delid3=0

#переменные для продовольствия
delrow4=0
delid4=0

#переменные для участников
delrow5=0
delid5=0

#переменные для оборудования
delrow6=0
delid6=0

#переменная для проверки страховки и билета
checkpos=0

class MainWindow(QWidget, form_class):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        self.setupUi(self)

#показывает информацию при клике
    def showfirminfo(self, a, b):
        while self.tableWidget_11.rowCount() > 0:
            self.tableWidget_11.removeRow(0)
        while self.tableWidget_10.rowCount() > 0:
            self.tableWidget_10.removeRow(0)
        firmid = int(self.tableWidget_9.item(a,0).text())
        rtinf = functions.firm_to_route(firmid)
        gds= functions.firm_to_guide(firmid)
        if rtinf:
            showroutetable(rtinf)
        if gds:
            showguidetable(gds)

    def showhikeinfo(self, a, b):
        while self.tableWidget_2.rowCount() > 0:
            self.tableWidget_2.removeRow(0)
        while self.tableWidget_3.rowCount() > 0:
            self.tableWidget_3.removeRow(0)
        hikeid = int(self.tableWidget.item(a,0).text())
        fdinf = functions.hike_to_food(hikeid)
        mminf= functions.hike_to_member(hikeid)
        if fdinf:
            showfoodtable(fdinf)
        if mminf:
            global ind1
            ind1=0
            showmembertable(mminf)

    def showmemberinfo(self, a, b):
        while self.tableWidget_4.rowCount() > 0:
            self.tableWidget_4.removeRow(0)
        membid = int(self.tableWidget_3.item(a,0).text())
        eqinf= functions.memb_to_equip(membid)
        if eqinf:
            showequipmenttable(eqinf)

#кнопки проверки страховки и билета

    def checkposition(self, a, b):
        global checkpos
        checkpos = int(self.tableWidget_3.item(a,0).text())

    def checkinsurance(self):
        global checkpos
        if not checkpos == 0:
            s = functions.showinsurance(checkpos)
            chkins=CheckInsClass.CheckInsWindow(self)
            chkins.setWindowTitle('Check insurance')
            if s:
                chkins.lineEdit.setText(s[0])
                chkins.lineEdit_2.setText(s[1])
                chkins.textEdit.setText(s[2])
            chkins.show()


    def checkticket(self):
        global checkpos
        if not checkpos == 0:
            s = functions.showticket(checkpos)
            chktck=CheckTickClass.CheckTickWindow(self)
            chktck.setWindowTitle('Check ticket')
            if s:
                chktck.lineEdit.setText(s[0])
                chktck.lineEdit_2.setText(s[1])
                chktck.lineEdit_3.setText(s[2])
            chktck.show()

#кнопки добавления

    def addhikebutt(self):
        addhike= AddHikeClass.AddHikeWindow(self)
        addhike.setWindowTitle('Add hike')
        addhike.addcomboboxitems()
        addhike.dateEdit.setCalendarPopup(True)
        addhike.dateEdit_2.setCalendarPopup(True)
        addhike.show()

    def addfoodbutt(self):
        addfood=AddFoodClass.AddFoodWindow(self)
        addfood.setWindowTitle('Add foodstuff')
        addfood.show()

    def addmemberbutt(self):
        addmember= AddMemberClass.AddMemberWindow(self)
        addmember.setWindowTitle('Add member')
        addmember.show()

    def addequipmentbutt(self):
        addequipment= AddEquipmentClass.AddEquipmentWindow(self)
        addequipment.setWindowTitle('Add equipment')
        addequipment.show()

    def addfirmbutt(self):
        addfirm= AddFirmClass.AddFirmWindow(self)
        addfirm.setWindowTitle('Add firm')
        addfirm.show()

    def addguidebutt(self):
        addguide= AddGuideClass.AddGuideWindow(self)
        addguide.setWindowTitle('Add guide')
        addguide.show()

    def addroutebutt(self):
        addroute= AddRouteClass.AddRouteWindow(self)
        addroute.setWindowTitle('Add route')
        addroute.show()

#редактирование и удаление фирм
    def checkentfirm(self):
        global ind
        ind=1

    def editfirm(self, a, b):
        global ind
        if ind == 1:
            if not b == 0:
                val = self.tableWidget_9.item(a,b)
                i=self.tableWidget_9.item(a,0)
                functions.changefirmdb(i.text(), val.text(), b)

    def checkdelfirm(self,a,b):
        global delrow, delid
        delrow = a
        delid = int(self.tableWidget_9.item(a,0).text())

    def delfirmbutt(self):
        global delrow, delid
        self.tableWidget_9.removeRow(delrow)
        functions.deletefirmdb(delid)
        while self.tableWidget_11.rowCount() > 0:
            self.tableWidget_11.removeRow(0)
        while self.tableWidget_10.rowCount() > 0:
            self.tableWidget_10.removeRow(0)

#редактирование и удаление маршрутов

    def checkentroute(self):
        global ind
        ind=1

    def editroute(self, a, b):
        global ind
        if ind == 1:
            if not b == 0:
                val = self.tableWidget_11.item(a,b)
                i=self.tableWidget_11.item(a,0)
                functions.changeroutedb(i.text(), val.text(), b)

    def checkdelroute(self,a,b):
        global delrow1, delid1
        delrow1 = a
        delid1 = int(self.tableWidget_11.item(a,0).text())

    def delroutebutt(self):
        global delrow1, delid1
        self.tableWidget_11.removeRow(delrow1)
        functions.deleteroutedb(delid1)

#редактирование и удаление проводников
    def checkentguide(self):
        global ind
        ind=1

    def editguide(self, a, b):
        global ind
        if ind == 1:
            if not b == 0:
                val = self.tableWidget_10.item(a,b)
                i=self.tableWidget_10.item(a,0)
                functions.changeguidedb(i.text(), val.text(), b)

    def checkdelguide(self,a,b):
        global delrow1, delid1
        delrow1 = a
        delid1 = int(self.tableWidget_10.item(a,0).text())

    def delguidebutt(self):
        global delrow1, delid1
        self.tableWidget_10.removeRow(delrow1)
        functions.deleteguidedb(delid1)

#редактирование и удаление походов
    def checkenthike(self):
        global ind
        ind=1

    def edithike(self, a, b):
        global ind
        if ind == 1:
            if not b == 0:
                val = self.tableWidget.item(a,b)
                i=self.tableWidget.item(a,0)
                functions.changehikedb(i.text(), val.text(), b)

    def checkdelhike(self, a, b):
        global delrow3, delid3
        delrow3 = a
        delid3 = int(self.tableWidget.item(a,0).text())

    def delhikebutt(self):
        global delrow3, delid3
        self.tableWidget.removeRow(delrow3)
        functions.deletehikedb(delid3)
        while self.tableWidget_2.rowCount() > 0:
            self.tableWidget_2.removeRow(0)
        while self.tableWidget_3.rowCount() > 0:
            self.tableWidget_3.removeRow(0)
        while self.tableWidget_4.rowCount() > 0:
            self.tableWidget_4.removeRow(0)

#редактирование и удаление продовольствия
    def checkentfood(self):
        global ind2
        ind2=1

    def editfood(self, a, b):
        global ind2
        if ind2 == 1:
            if not b == 0:
                val = self.tableWidget_2.item(a,b)
                i=self.tableWidget_2.item(a,0)
                functions.changefooddb(i.text(), val.text(), b)

    def checkdelfood(self,a,b):
        global delrow4, delid4
        delrow4 = a
        delid4 = int(self.tableWidget_2.item(a,0).text())

    def delfoodbutt(self):
        global delrow4, delid4
        self.tableWidget_2.removeRow(delrow4)
        functions.deletefooddb(delid4)

#редактирование и удаление участников
    def checkentmember(self):
        global ind1
        ind1=1

    def editmember(self, a, b):
        global ind1
        if ind1 == 1:
            if not b == 0:
                val = self.tableWidget_3.item(a,b)
                i=self.tableWidget_3.item(a,0)
                functions.changememberdb(i.text(), val.text(), b)

    def checkdelmember(self,a,b):
        global delrow5, delid5
        delrow5 = a
        delid5 = int(self.tableWidget_3.item(a,0).text())

    def delmemberbutt(self):
        global delrow5, delid5
        self.tableWidget_3.removeRow(delrow5)
        functions.deletememberdb(delid5)
        while self.tableWidget_4.rowCount() > 0:
            self.tableWidget_4.removeRow(0)

#редактирование и удаление оборудование
    def checkentequipment(self):
        global ind3
        ind3=1

    def editequipment(self, a, b):
        global ind3
        if ind3 == 1:
            if not b == 0:
                val = self.tableWidget_4.item(a,b)
                i=self.tableWidget_4.item(a,0)
                functions.changeequipmentdb(i.text(), val.text(), b)

    def checkdelequipment(self,a,b):
        global delrow6, delid6
        delrow6 = a
        delid6 = int(self.tableWidget_4.item(a,0).text())

    def delequipmentbutt(self):
        global delrow6, delid6
        self.tableWidget_4.removeRow(delrow6)
        functions.deleteequipmentdb(delid6)

#обновление таблиц
    def updatebutt(self):
        while self.tableWidget_9.rowCount() > 0:
            self.tableWidget_9.removeRow(0)
        showfirmtable()

    def updatebutt1(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        showhiketable()

#-----------------------------------------------------#
form = MainWindow()
form.setWindowTitle('Hike DB')
form.setWindowIcon(QIcon('hike.ico'))

#изменяем ширину столбцов
#-----------------------------------------------------#
form.tableWidget.setSortingEnabled(True) #сортировка
form.tableWidget.setColumnWidth(0, 20)
form.tableWidget.setColumnWidth(7, 70)
form.tableWidget.setColumnWidth(8, 108)

form.tableWidget_3.setSortingEnabled(True) #сортировка
form.tableWidget_3.setColumnWidth(0, 20)
form.tableWidget_3.setColumnWidth(1, 178)
form.tableWidget_3.setColumnWidth(5, 200)

form.tableWidget_2.setSortingEnabled(True) #сортировка
form.tableWidget_2.setColumnWidth(0, 20)
form.tableWidget_2.setColumnWidth(1, 135)
form.tableWidget_2.setColumnWidth(2, 135)

form.tableWidget_4.setSortingEnabled(True) #сортировка
form.tableWidget_4.setColumnWidth(0, 20)
form.tableWidget_4.setColumnWidth(1, 40)
form.tableWidget_4.setColumnWidth(2, 80)
form.tableWidget_4.setColumnWidth(3, 70)
form.tableWidget_4.setColumnWidth(4, 80)

form.tableWidget_9.setSortingEnabled(True) #сортировка
form.tableWidget_9.setColumnWidth(0, 40)
form.tableWidget_9.setColumnWidth(1, 182)
form.tableWidget_9.setColumnWidth(2, 175)

form.tableWidget_10.setSortingEnabled(True) #сортировка
form.tableWidget_10.setColumnWidth(0, 40)
form.tableWidget_10.setColumnWidth(1, 190)
form.tableWidget_10.setColumnWidth(2, 90)
form.tableWidget_10.setColumnWidth(3, 90)

form.tableWidget_11.setSortingEnabled(True) #сортировка
form.tableWidget_11.setColumnWidth(0, 40)
form.tableWidget_11.setColumnWidth(1, 220)
form.tableWidget_11.setColumnWidth(2, 154)
form.tableWidget_11.setColumnWidth(3, 100)
form.tableWidget_11.setColumnWidth(4, 90)
form.tableWidget_11.setColumnWidth(5, 100)
form.tableWidget_11.setColumnWidth(6, 140)
#-----------------------------------------------------#


#show tables
#-----------------------------------------------------#

#показывает фирмы
def showfirmtable():
    rows = functions.showrowinfirms()
    for row in rows:
        functions.table_appender(form.tableWidget_9, row)
showfirmtable()

#показывает маршруты
def showroutetable(rtinf):
    for row in rtinf:
        functions.table_appender(form.tableWidget_11, row)

#показывает проводников
def showguidetable(gdinf):
    for row in gdinf:
        functions.table_appender(form.tableWidget_10, row)

#показывает походы
def showhiketable():
    rows = functions.showrowinhikes()
    for row in rows:
        functions.table_appender(form.tableWidget, row)
showhiketable()

#показывает продовольствие
def showfoodtable(fdinf):
    for row in fdinf:
        functions.table_appender(form.tableWidget_2, row)

#показывает участников
def showmembertable(mminf):
    for row1 in mminf:
        functions.table_appender(form.tableWidget_3, row1)

#показывает оборудование
def showequipmenttable(eqinf):
    for row in eqinf:
        functions.table_appender(form.tableWidget_4, row)

form.show()
sys.exit(app.exec_())