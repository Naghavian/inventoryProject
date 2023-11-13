from PyQt5 import QtCore, QtGui, QtWidgets
import threading # Example Hojat For " For " And Contunue After For But For Is Running
import sys, qdarkstyle # Dark Style Theme
from time import sleep
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
from datetime import datetime
import jalali,sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.DataBasbeConncet()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(1023, 899)
        self.Dialog.setFixedSize(self.Dialog.size()) # Set Size Fixed
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(440, 10, 151, 51))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 981, 831))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(25, 40, 571, 771))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Price','Customer','Admin','Date'])
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # Lock Editting Table Live
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(620, 30, 231, 161))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(80, 30, 141, 31))
        self.label_7.setText(self.datejalali()) # Jalali Date
        self.label_7.setObjectName("label_7")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_6)
        self.lcdNumber_2.setGeometry(QtCore.QRect(10, 80, 131, 61))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        threading.Thread(target=self.showTime,daemon=True).start()
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(620, 210, 321, 411))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 30, 301, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 81, 41))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 181, 41))
        self.comboBox.setObjectName("comboBox")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 140, 301, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 40, 161, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(6, 40, 111, 41))
        self.label_5.setObjectName("label_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 250, 301, 81))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 281, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 340, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 340, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_7.setGeometry(QtCore.QRect(620, 637, 321, 171))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 70, 141, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.BackButtonClicked) # Back Button Clicked 
        self.FillTableNoFilter()
        self.FillComboBoxAdmin()
        self.FillComboBoxUser()
        self.pushButton_2.clicked.connect(self.FillTableNoFilter)
        self.pushButton.clicked.connect(self.FillTableFilter)
        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Invoices")) # Main Window Title
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">View Invoices</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("Dialog", "Date/Time"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Date:</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Dialog", "Filters"))
        self.groupBox_3.setTitle(_translate("Dialog", "Select Admin"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Admin:</span></p></body></html>"))
        self.groupBox_4.setTitle(_translate("Dialog", "Select Customer"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Customer:</span></p></body></html>"))
        self.groupBox_5.setTitle(_translate("Dialog", "Enter Date"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "               Enter Like: YYYY/MM/DD"))
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))
        self.pushButton_3.setText(_translate("Dialog", "Back"))
    def DataBasbeConncet(self): # Connecting to DataBase
        self.db = sqlite3.connect("/home/moein/Documents/MainProject/Project.db")
    def datejalali(self): # Jalali Date Receiver
        return str(jalali.Gregorian(datetime.today().strftime('%Y-%m-%d')).persian_string())
    def BackButtonClicked(self): # Def Back Push Button Click - Goes To Perv Page ( Sotre Page )
        from Store import Ui_Dialog as StorePG
        self.Store_PG = QtWidgets.QMainWindow()
        self.Store_UI = StorePG()
        self.Store_UI.setupUi(self.Store_PG)
        self.Dialog.close()
        self.Store_PG.show()
    def showTime(self):
        
        while True:
            time = QTime.currentTime()
            text = time.toString('hh:mm')
            if (time.second() % 2) == 0:
                text = text[:2] + ' ' + text[3:]
            self.lcdNumber_2.display(text)
            sleep(1) # If We Don't use This , CPU Usage Goes 100%
    def FillTableNoFilter(self):
        data = self.db.execute('select Price,CustomerID,AdminID,Date from Invoices')
        rows = 0 # The number of the row * that there is the Goods table
        sales = []
        UserName = str()
        AdminName = str()
        for i in data:
            sales.append(i)
            
            rows += 1
        self.tableWidget.setRowCount(rows)#number of the row in tabale

        for row in range(rows):
            for column in range(4):
                if column == 1:
                    d = self.db.execute('select Name from Customers where ID = {}'.format(sales[row][column]))#################
                    for i in d:
                        UserName = i[0]
                    newItem = QtWidgets.QTableWidgetItem(UserName)
                    self.tableWidget.setItem(row, column, newItem)
                    UserName = ''
                elif column == 2:
                    newItem = QtWidgets.QTableWidgetItem(sales[row][column])
                    self.tableWidget.setItem(row, column, newItem)
                    AdminName = ''
                else:
                    newItem = QtWidgets.QTableWidgetItem(str(sales[row][column]))
                    self.tableWidget.setItem(row, column, newItem)
        self.lineEdit.setText("")     
    def FillComboBoxAdmin(self): # it fill the combobox of the admin
        data = self.db.execute('select Name from Admins') # get the name of the admin from data base
        self.comboBox.addItem('All')
        for i in data:
            self.comboBox.addItem(str(i[0]))       
    def FillComboBoxUser(self): # it fill the combobox of the Customer
            data = self.db.execute('select Name from Customers') # get the name of the customer from data base
            self.comboBox_2.addItem('All')

            for i in data:
                self.comboBox_2.addItem(str(i[0]))            
    def FillTableFilter(self):
        data = str()
        date = self.lineEdit.text()
        admin = self.comboBox.currentText()
        user = self.comboBox_2.currentText()

        if (date != '' and admin == 'All' and user == 'All'):
            data = self.db.execute(
                'select Price,CustomerID,AdminID,Date from Invoices where Date = \'{}\''.format(date)
            )
            
        elif (date == '' and admin != 'All' and user == 'All'):
            data = self.db.execute(
                'select Price,CustomerID,AdminID,Date from Invoices where AdminID = \'{}\''.format(admin)
            )
            
        elif (date == '' and admin == 'All' and user != 'All'):
            
            Query = self.db.execute('select ID from Customers where Name = \'{}\''.format(user))
            idOfUser= str()
            for i in Query:
                idOfUser = i[0]
            data = self.db.execute(
                'select Price,CustomerID,AdminID,Date from Invoices where CustomerID = \'{}\''.format(idOfUser)
            )
        elif (date != '' and admin != 'All' and user == 'All'):
            data = self.db.execute(
                'select Price,CustomerID,AdminID,Date from Invoices where Date = \'{}\' and AdminID = \'{}\''.format(date,admin)
            )
        elif (date != '' and admin == 'All' and user != 'All'):
            Query = self.db.execute('select ID from Customers where Name = \'{}\''.format(user))
            idOfUser= str()
            for i in Query:
                idOfUser = i[0]
            data = self.db.execute(
                'select Price,CustomerID,AdminID,Date from Invoices where Date = \'{}\' and CustomerID = \'{}\''.format(date,idOfUser)
            )
        elif (date == '' and admin != 'All' and user != 'All'):
            Query = self.db.execute('select ID from Customers where Name = \'{}\''.format(user))
            idOfUser= str()
            for i in Query:
                idOfUser = i[0]
            data = self.db.execute(
                'select Price,CustomerID,AdminID,Date from Invoices where AdminID = \'{}\' and CustomerID = \'{}\''.format(admin,idOfUser)
            )
        elif (date != '' and admin != 'All' and user != 'All'):
            Query = self.db.execute('select ID from Customers where Name = \'{}\''.format(user))
            idOfUser= str()
            for i in Query:
                idOfUser = i[0]
            data = self.db.execute(
                'select Price,CustomerID,AdminID,Date from Invoices where Date = \'{}\' and AdminID = \'{}\' and CustomerID = \'{}\''.format(date,admin,idOfUser)
            )
        else:
            data = self.db.execute(
                'select Price,CustomerID,AdminID,Date from Invoices'
            )
        rows = 0 # The number of the row * that there is the Goods table
        sales = []
        UserName = str()
        AdminName = str()
        for i in data:
            sales.append(i)
            rows += 1
        self.tableWidget.setRowCount(rows)#number of the row in tabale

        for row in range(rows):
            for column in range(4):
                if column == 1:
                    d = self.db.execute('select Name from Customers where ID = {}'.format(sales[row][column]))#################
                    for i in d:
                        UserName = i[0]
                    newItem = QtWidgets.QTableWidgetItem(UserName)
                    self.tableWidget.setItem(row, column, newItem)
                    UserName = ''
                elif column == 2:
                    newItem = QtWidgets.QTableWidgetItem(sales[row][column])
                    self.tableWidget.setItem(row, column, newItem)
                    AdminName = ''
                else:
                    newItem = QtWidgets.QTableWidgetItem(str(sales[row][column]))
                    self.tableWidget.setItem(row, column, newItem)
if __name__ == '__main__':
    window = QtWidgets.QApplication(sys.argv)
    window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # Dark Style Theme
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(window.exec_())