from PyQt5 import QtCore, QtGui, QtWidgets
import sys, qdarkstyle # Dark Style Theme
from SignUpNewCustomer import Ui_Dialog as SignUpPG
import threading # Example Hojat For " For " And Contunue After For But For Is Running
from time import sleep
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
from datetime import datetime
import jalali,sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.DataBasbeConncet() # Call The Def - Connects To Data Base
        self.CustomerID = int()
        self.total = 0
        self.Invoices = list()
        Dialog.setObjectName("Dialog")
        Dialog.resize(1110, 886)
        Dialog.setFixedSize(Dialog.size()) # Set Size Fixed
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 1081, 821))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 231, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 141, 31))
        self.label_3.setText(self.datejalali()) # Insert Date STR Into The Label
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 80, 120, 45))
        self.lcdNumber.setObjectName("lcdNumber")
        threading.Thread(target=self.showTime,daemon=True).start()
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 30, 251, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(80, 30, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('None') # When Seller Didn't Chose Any Customer , Combobox Shows "None"
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(45, 70, 199, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 33, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 110, 111, 41))
        self.pushButton_2.clicked.connect(self.OpenSignUpNewCustomerPage) # Connect to def Open Sign Up New Customer Page
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 65, 31))
        self.label_5.setObjectName("label_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(550, 30, 241, 161))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 33, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(43, 30, 188, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 71, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 70, 151, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 110, 221, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.SubmitButtonClicked) # Connect to def Submit Button Clicked
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(820, 30, 241, 161))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(110, 29, 121, 31))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(10, 110, 221, 41))
        self.label_11.setObjectName("label_11")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 200, 511, 551))
        self.groupBox_6.setObjectName("groupBox_6")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_6)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 491, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4) # Column Counter
        self.tableWidget.setHorizontalHeaderLabels(['ID','Name','Price','Count'])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # Lock Editting Table Live
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_7.setGeometry(QtCore.QRect(550, 200, 511, 551))
        self.groupBox_7.setObjectName("groupBox_7")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 30, 491, 511))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4) # Column Counter
        self.tableWidget_2.setHorizontalHeaderLabels(['ID','Name','Price','Count'])
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # Lock Editting Table Live
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 760, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(960, 760, 101, 41))
        self.pushButton_5.clicked.connect(self.BackButtonClicked)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 760, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.OpenViewInvoicesPG)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(510, 10, 81, 41))
        self.label.setObjectName("label")
        self.FillTable() # Call Def Fill Table And Fills Table
        self.pushButton.clicked.connect(self.SubmitButtonClicked_2) # Select Customer Submit Button
        self.FillComboBox() # Call Def Fill ComboBox - Fills From Data Base
        self.pushButton_4.clicked.connect(self.FinishButtonClicked) # Finish Button
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def FinishButtonClicked(self): # Finish Button - 
        data = self.label_3.text() # Gets Date
        AdminName = self.label_9.text() # Gets Admin Name - Using To Find Admin ID From Data Base
        x = self.db.execute('select ID from Admins where Name=\'{}\''.format(AdminName)) # Gets Admin ID Using Admin Name To Find
        AdminID = str()
        for i in x:
            AdminID = i[0]
        self.db.execute('insert into Invoices (AdminID,CustomerID,Price,Date) values (\'{}\',{},{},\'{}\')'.format(AdminID,self.CustomerID,self.total,data))
        self.db.commit()
        data=self.db.execute('select MAX(ID) from Invoices ')
        InvoiceID = int()
        for i in data:
            InvoiceID = i[0]
        for i in self.Invoices:
            self.db.execute('insert into InvoiceInfo (InvoiceID,ProductID,Counter,Price) values ({},{},{},{})'.format(InvoiceID,i[0],i[1],i[2]))
            self.db.commit()
            self.tableWidget.setRowCount(0)
            self.total = 0
            _translate = QtCore.QCoreApplication.translate
            self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">0</span></p></body></html>"))
    def FillComboBox(self):
        data = self.db.execute('select Name from Customers')
        for i in data:
            self.comboBox.addItem(i[0])
    def SubmitButtonClicked_2(self):

        Name = self.comboBox.currentText()
        ID = self.lineEdit.text()
        if Name != 'None':
            data = self.db.execute('select ID from Customers where Name=\'{}\''.format(Name))
            for i in data:
                self.CustomerID = i[0]
        else:
            self.CustomerID = ID
        print(self.CustomerID)
    def datejalali(self): # Jalali Date Receiver
        return str(jalali.Gregorian(datetime.today().strftime('%Y-%m-%d')).persian_string())
    def FillTable(self): # Fills Table Using Data Base From Seller Selected Items For Product
        data = self.db.execute('select ID,Name,Price,Counter from Products;')
        products=list()
        RowCounter = 0
        for i in data:
            products.append(i)
            RowCounter += 1
        self.tableWidget_2.setRowCount(RowCounter)
        for row in range(self.tableWidget_2.rowCount()):
            for column in range(self.tableWidget_2.columnCount()):
                newItem = QtWidgets.QTableWidgetItem(str(products[row][column]))
                self.tableWidget_2.setItem(row, column, newItem)
    def DataBasbeConncet(self): # Connecting to DataBase
        self.db = sqlite3.connect("/home/moein/Documents/MainProject/Project.db")
    def OpenSignUpNewCustomerPage(self): # Opens Sign Up New Customer Page And We Can Do Changes...
        self.SignUp_PG = QtWidgets.QMainWindow()
        self.SignUpNewCustomerUi = SignUpPG()
        self.SignUpNewCustomerUi.setupUi(self.SignUp_PG)
        self.SignUp_PG.show()
    def showTime(self): # Show Time From Import Time To LCD Number
        while True:
            time = QTime.currentTime()
            text = time.toString('hh:mm')
            if (time.second() % 2) == 0:
                text = text[:2] + ' ' + text[3:]
            self.lcdNumber.display(text)
            sleep(1) # If We Don't use This , CPU Usage Goes 100%
    def BackButtonClicked(self): # Def Back Push Button Click - Goes To Perv Page ( Log In Page )
        from Login import Ui_Dialog as LoginPG
        self.Login_PG = QtWidgets.QMainWindow()
        self.Login_UI = LoginPG()
        self.Login_UI.setupUi(self.Login_PG)
        self.Dialog.close()
        self.Login_PG.show()
    def OpenViewInvoicesPG(self): # Opens View Invoices Page And We Can Do Changes...
        from ViewInvoices import Ui_Dialog as ViewInvoicesPG
        self.ViewInvoices_PG = QtWidgets.QMainWindow()
        self.ViewInvoicesUi = ViewInvoicesPG()
        self.ViewInvoicesUi.setupUi(self.ViewInvoices_PG)
        self.ViewInvoices_PG.show()
    def SubmitButtonClicked(self): # Product Submit Button Fills Table Saled
        ID = self.lineEdit_2.text()
        Count = self.lineEdit_3.text()
        Flag = False
        try:
            SelectID = self.db.execute('SELECT Price,Name,Counter,ID FROM Products WHERE ID = {}'.format (ID))
            Flag = True
        except: pass
        Price = 0
        Name = str()
        HaveCount = 0
        for i in SelectID:
            HaveCount = i[2]
            Name = i[1]
            Price = i[0]
            ID = i[3]
            
            print('Price=' , Price)
            print('Count= ',Count)
            print('WeCOunt= ',HaveCount)        
        if Flag:
            if int(Count) <= int(HaveCount):
                self.Invoices.append([ID,Count,int(Price)*int(Count)])
                self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                row = self.tableWidget.rowCount() - 1
                newItem = QtWidgets.QTableWidgetItem(str(ID))
                self.tableWidget.setItem(row, 0, newItem)
                newItem = QtWidgets.QTableWidgetItem(str(Name))
                self.tableWidget.setItem(row, 1, newItem)
                newItem = QtWidgets.QTableWidgetItem(str(int(Price)*int(Count)))
                self.tableWidget.setItem(row, 2, newItem)
                newItem = QtWidgets.QTableWidgetItem(str(Count))
                self.tableWidget.setItem(row, 3, newItem)
                NewCount = int(HaveCount) - int(Count)
                self.db.execute('update Products set Counter={} where ID={}'.format(NewCount,ID))
                self.db.commit()
                self.FillTable()
                self.total += (int(Price)*int(Count))
                _translate = QtCore.QCoreApplication.translate
                self.label_11.setText((_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">{}</span></p></body></html>".format(self.total))))
            else:
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_2.setPlaceholderText('No Enough Products')      
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sale")) # Main Window Title
        self.groupBox_2.setTitle(_translate("Dialog", "Date/Time"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Date:</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("Dialog", "Customer"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ID:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.pushButton_2.setText(_translate("Dialog", "Sign Up"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Name:</span></p></body></html>"))
        self.groupBox_4.setTitle(_translate("Dialog", "Product"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ID:</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Count:</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Dialog", "Submit"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Loged in as:</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Total(Rials):</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">0</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("Dialog", "Sales"))
        self.groupBox_7.setTitle(_translate("Dialog", "Products"))
        self.pushButton_4.setText(_translate("Dialog", "Finish"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">Sale</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Dialog", "Back"))
        self.pushButton_6.setText(_translate("Dialog", "View Invoices"))

if __name__ == '__main__':
    window = QtWidgets.QApplication(sys.argv)
    window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # Dark Style Theme
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(window.exec_())

