from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qdarkstyle # Dark Stle Theme
import sqlite3

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.DataBasbeConncet()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(440, 592)
        self.Dialog.setFixedSize(self.Dialog.size()) # Fixed Size
        self.groupBox = QtWidgets.QGroupBox(self.Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 30, 361, 531))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 30, 301, 471))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 221, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(40, 40, 67, 30))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 160, 221, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 67, 30))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 250, 221, 51))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 67, 30))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 330, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 390, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.CancelClickedButton)
        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
    def DataBasbeConncet(self): # Connecting to DataBase
        self.db = sqlite3.connect("/home/moein/Documents/MainProject/Project.db")
    def CancelClickedButton(self): # Def Cancel Button Clicked
        self.Dialog.close()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit items")) # MAin Window Title
        self.groupBox.setTitle(_translate("Dialog", "Edit"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID:</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Price:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Count:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Edit"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))

 
        
    
if __name__ == '__main__':
    window = QtWidgets.QApplication(sys.argv)
    window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) #Dark Style Theme
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(window.exec_())