from PyQt5 import QtCore, QtGui, QtWidgets
import sys , qdarkstyle # DarkStyle Theme
import sqlite3
from Store import Ui_Dialog as StorePG # Import Store Page Ui
from Sale import Ui_Dialog as SalePG # Import Sale Page Ui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(667, 788)
        font = QtGui.QFont()
        font.setPointSize(15)

        self.Dialog.setFixedSize(self.Dialog.size()) # Fixed Size

        self.DataBasbeConncet()
        self.groupBox = QtWidgets.QGroupBox(self.Dialog)
        self.groupBox.setGeometry(QtCore.QRect(120, 90, 401, 571))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 160, 361, 371))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 59))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 70, 321, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 101, 59))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 160, 321, 41))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 270, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit) #Qiut Button - Quit The Whole Program

        self.pushButton_2.setGeometry(QtCore.QRect(190, 270, 131, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 341, 81))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 760, 67, 17))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 321, 41)) # ERR Label
        self.label_5.setObjectName("label_5")
        
        
        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.LoginButtonClicked) # Connects To DEf LoginButtonClicked

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Log in Page")) # Main Window Title
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Username:</span></p></body></html>"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Enter Username..."))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter Password..."))
        self.pushButton.setText(_translate("Dialog", "Connect"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Log in</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "V 1.1.0.0."))
    def DataBasbeConncet(self): # Connecting to DataBase
        self.db = sqlite3.connect("/home/moein/Documents/MainProject/Project.db")
    
    def LoginButtonClicked(self): # Button "Connect" On Login Page - "userid" And " userpass" Receive From LinedEdits 
        userid = self.lineEdit_2.text()
        userpass = self.lineEdit.text()
        database = self.db.execute('SELECT * FROM Admins WHERE ID=\'{}\';'.format(userid)) # Receiving The Data From Database Based On Entered Username
        Name = str()
        Password = str()
        Code = str()
        for x in database:
            Name = x[1]
            Password = x[2]
            Code = x[3]
        if Password == userpass and Code == 0:
            self.AdminName = Name
            self.OpenStorePG()
            self.Dialog.close()
        elif Password == userpass and Code == 1:
            self.AdminName = Name
            self.OpenSalePG()
            self.Dialog.close()
        else:
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.label_5.setText(("<html><head/><body><p><span style=\" font-size:12pt; color:#cc0000;\">Invalid Username or Password!!!</span><br/></p></body></html>"))
            # Appears When USer Enters An Invalid Username Or Password

    def OpenStorePG(self): # Opens Store Page And We Can Do Changes...
        self.Store_PG = QtWidgets.QMainWindow()
        self.StoreUi = StorePG()
        self.StoreUi.setupUi(self.Store_PG)
        self.StoreUi.label_3.setText(self.AdminName)
        self.Store_PG.show()

    def OpenSalePG(self): # Opens Sale Page And We Can Do Changes...
        self.Sale_PG = QtWidgets.QMainWindow()
        self.SaleUi = SalePG()
        self.SaleUi.setupUi(self.Sale_PG)
        self.SaleUi.label_9.setText(self.AdminName)
        self.Sale_PG.show()
if __name__ == '__main__':
    window = QtWidgets.QApplication(sys.argv)
    window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # Dark Style Theme
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(window.exec_())
    