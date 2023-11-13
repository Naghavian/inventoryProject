from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5,sqlite3
import sys, qdarkstyle #Darkstyle Theme
import jalali # jalali Calendar
from datetime import datetime
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
import threading # Example Hojat For " For " And Contunue After For But For Is Running
from time import sleep # Time Puase For Every Sec - Managing CPU Usage
from Edititem import Ui_Dialog as EdititemPG # Import Edit Item Page Ui
from ViewInvoices import Ui_Dialog as ViewInvoicesPG # Import View Invoices Page Ui



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.DataBasbeConncet() # Call The Def - Connects To Data Base
        self.Dialog = Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(1112, 887)
        self.Dialog.setFixedSize(self.Dialog.size()) # Fixed Size
        self.groupBox = QtWidgets.QGroupBox(self.Dialog)
        self.groupBox.setGeometry(QtCore.QRect(110, 90, 891, 781))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(560, 410, 111, 41))
        self.pushButton.clicked.connect(self.OpenAdditemPG) # Connect to def Open Add item Page
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 480, 111, 41))
        self.pushButton_2.clicked.connect(self.OpenEditItemPG) # Connect to def Open Add item Page
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 690, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.clicked.connect(QtCore.QCoreApplication.instance().quit) # Quit Button - Quits The Whole Program
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 620, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(570, 70, 120, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(570, 110, 60, 30))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 550, 111, 41))
        self.pushButton_5.clicked.connect(self.OpenViewInvoicesPG) # Connect to def Open View Invoices Page
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(690, 70, 181, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(35, 61, 501, 671))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4) # Column Counter
        self.tableWidget.setHorizontalHeaderLabels(['ID','Name','Price','Count']) # Set Columns Names
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # Lock Editting Table Live
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox) # Date And Time GroupBox
        self.groupBox_2.setGeometry(QtCore.QRect(570, 100, 230, 121))# Date And Time GroupBox
        self.groupBox_2.setObjectName("groupBox_2") # Date And Time GroupBox
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_2) # Date And Time GroupBox
        self.lcdNumber.setGeometry(QtCore.QRect(10, 70, 120, 45))# Date And Time GroupBox
        self.lcdNumber.setObjectName("lcdNumber") # Date And Time GroupBox
        threading.Thread(target=self.showTime,daemon=True).start()

        self.label_2 = QtWidgets.QLabel(self.groupBox_2) # Date And Time GroupBox
        self.label_2.setGeometry(QtCore.QRect(10, 30, 59, 26))# Date And Time GroupBox
        self.label_2.setObjectName("label_2") # Date And Time GroupBox
        self.label_4 = QtWidgets.QLabel(self.groupBox_2) # Date And Time GroupBox
        self.label_4.setGeometry(QtCore.QRect(70, 30, 150, 31)) # Date And Time GroupBox
        self.label_4.setText(self.datejalali()) # Date And Time GroupBox - Jalali Calendar
        self.label_4.setObjectName("label_4") # Date And Time GroupBox
        self.pushButton_4.clicked.connect(self.BackButtonClicked) # Connects To Def Back Button Clicked
        #self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);") # Table Back Ground Color White
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(510, 30, 91, 51))
        self.label_5.setObjectName("label_5")
        self.FillTable() # Call Fill Table Def
        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
    def FillTable(self): # Fills The Table From Data Base
        data = self.db.execute('select ID,Name,Counter,Price from Products;')
        products=list()
        RowCounter = 0
        for i in data:
            products.append(i)
            RowCounter += 1
        self.tableWidget.setRowCount(RowCounter)
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                newItem = QtWidgets.QTableWidgetItem(str(products[row][column]))
                self.tableWidget.setItem(row, column, newItem)

    def datejalali(self): # Jalali Date Receiver
        return str(jalali.Gregorian(datetime.today().strftime('%Y-%m-%d')).persian_string())

    def showTime(self): # Def Show Time - Then We Use This On LCD Number Text
        while True:
            time = QTime.currentTime()
            text = time.toString('hh:mm')
            if (time.second() % 2) == 0:
                text = text[:2] + ' ' + text[3:]
            self.lcdNumber.display(text)
            sleep(1) # If We Don't use This , CPU Usage Goes 100%
    def DataBasbeConncet(self): # Connecting to DataBase
        self.db = sqlite3.connect("/home/moein/Documents/MainProject/Project.db")

    def BackButtonClicked(self): # Def Back Push Button Click - Goes To Perv Page ( Log In Page )
        from Login import Ui_Dialog as LoginPG
        self.Login_PG = QtWidgets.QMainWindow()
        self.Login_UI = LoginPG()
        self.Login_UI.setupUi(self.Login_PG)
        self.Dialog.close()
        self.Login_PG.show()

    def OpenAdditemPG(self): # Opens Additem Page And We Can Do Changes...
        from Additem import Ui_Dialog as AdditemPG # Import Add Item Page U
        self.Additem_PG = QtWidgets.QMainWindow()
        self.AdditemUi = AdditemPG()
        self.AdditemUi.setupUi(self.Additem_PG)
        # self.additemUi.lineEdit.setPlaceholderText("")
        # self.additemUi.lineEdit_2.setPlaceholderText("")
        # self.additemUi.lineEdit_3.setPlaceholderText("")
        self.Additem_PG.show()
        self.AdditemUi.pushButton.clicked.connect(self.AddButtonNew)

    def AddButtonNew(self):
        name = self.AdditemUi.lineEdit.text()
        price = self.AdditemUi.lineEdit_2.text()
        count = self.AdditemUi.lineEdit_3.text()
        try:

            self.db.execute('insert into Products (Name,Counter,Price) values (\'{}\',{},{})'.format(name,count,price))
            self.db.commit()
            self.AdditemUi.lineEdit.setText('')
            self.AdditemUi.lineEdit_2.setText('')
            self.AdditemUi.lineEdit_3.setText('')
            self.FillTable()
        except:
            self.AdditemUi.lineEdit.setText('')
            self.AdditemUi.lineEdit_2.setText('')
            self.AdditemUi.lineEdit_3.setText('')
            self.AdditemUi.lineEdit.setPlaceholderText("Invalid Input...")
            self.AdditemUi.lineEdit_2.setPlaceholderText("Invalid Input...")
            self.AdditemUi.lineEdit_3.setPlaceholderText("Invalid Input...")

    def OpenEditItemPG(self): # Opens Edit item Page And We Can Do Changes...
        self.Edititem_PG = QtWidgets.QMainWindow()
        self.EdititemUi = EdititemPG()
        self.EdititemUi.setupUi(self.Edititem_PG)
        self.Edititem_PG.show()
        self.EdititemUi.pushButton.clicked.connect(self.EditButtonStore)

    def EditButtonStore(self):
        try:
            self.EditID = int(self.EdititemUi.lineEdit.text())
            self.EditCount = int(self.EdititemUi.lineEdit_2.text())
            self.EditPrice = int(self.EdititemUi.lineEdit_3.text())
        except:
            self.EdititemUi.lineEdit.setPlaceholderText('Invalid Input...')
            self.EdititemUi.lineEdit_2.setPlaceholderText('Invalid Input...')
            self.EdititemUi.lineEdit_3.setPlaceholderText('Invalid Input...')
            self.EdititemUi.lineEdit.setText('')
            self.EdititemUi.lineEdit_2.setText('')
            self.EdititemUi.lineEdit_3.setText('')
            return False
        try:
            self.EdititemUi.lineEdit.setPlaceholderText('')
            self.EdititemUi.lineEdit_2.setPlaceholderText('')
            self.EdititemUi.lineEdit_3.setPlaceholderText('')
            self.db.execute('update Products set Price={} , Counter={} where ID={};'.format(self.EditPrice,self.EditCount,self.EditID))
            self.db.commit()
        except: 
            self.EdititemUi.lineEdit.setPlaceholderText('Error Quering DataBase...')
            self.EdititemUi.lineEdit_2.setPlaceholderText('Error Quering DataBase...')
            self.EdititemUi.lineEdit_3.setPlaceholderText('Error Quering DataBase...')
            self.EdititemUi.lineEdit.setText('')
            self.EdititemUi.lineEdit_2.setText('')
            self.EdititemUi.lineEdit_3.setText('')
            return False
        self.EdititemUi.lineEdit.setText('')
        self.EdititemUi.lineEdit_2.setText('')
        self.EdititemUi.lineEdit_3.setText('')
        self.FillTable()

    def OpenViewInvoicesPG(self): # Opens View Invoices Page And We Can Do Changes...
        self.ViewInvoices_PG = QtWidgets.QMainWindow()
        self.ViewInvoicesUi = ViewInvoicesPG()
        self.ViewInvoicesUi.setupUi(self.ViewInvoices_PG)
        self.ViewInvoices_PG.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Store")) # Main Window Title
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.pushButton_2.setText(_translate("Dialog", "Edit"))
        self.pushButton_3.setText(_translate("Dialog", "Exit"))
        self.pushButton_4.setText(_translate("Dialog", "Back"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Loged in as:</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Date:</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Dialog", "Date/Time"))
        self.pushButton_5.setText(_translate("Dialog", "Invoices"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Store</span></p></body></html>"))

if __name__ == '__main__':
    window = QtWidgets.QApplication(sys.argv)
    window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # Dark style Theme
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(window.exec_())