from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle # Dark Style Theme
import sys,sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.Dialog.setObjectName("Dialog")
        self.DataBasbeConncet()
        self.Dialog.setFixedSize(482, 355) # Set Fixed Size For Fixing The Size
        #self.Dialog.setFixedSize(self.Dialog.size()) # Fixed Size
        self.groupBox = QtWidgets.QGroupBox(self.Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 441, 321))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 90, 281, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 240, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 240, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(80, 150, 281, 81))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 41, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(60, 30, 211, 41))
        self.label_3.setText("\"Generated ID appears here!\"") # This Text Will Be Removed - Generated ID From Data Base Appears
        self.label_3.setObjectName("label_3")
        self.pushButton.clicked.connect(self.AddButtonClicked)
        self.pushButton_2.clicked.connect(self.CancelButtonClicked)
        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
    def AddButtonClicked(self):
        name = self.lineEdit.text()
        if name != '':
            self.db.execute('insert into Customers (Name) Values (\'{}\')'.format(name))
            data = self.db.execute('select ID from Customers where Name=\'{}\''.format(name))
            self.db.commit()
            id = int()
            for i in data:
                id = i[0]
            self.label_3.setText(str(id))
            self.lineEdit.setText('')
            self.lineEdit.setPlaceholderText('Done...')
    def CancelButtonClicked(self):
        self.Dialog.close()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign Up New Customer")) # Main Window Title
        self.groupBox.setTitle(_translate("Dialog", "Sign Up New Customer"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter Customer\'s Full Name...."))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Name:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ID :</span></p></body></html>"))

    def DataBasbeConncet(self): # Connecting to DataBase
        self.db = sqlite3.connect("/home/moein/Documents/MainProject/Project.db")
if __name__ == '__main__':
    window = QtWidgets.QApplication(sys.argv)
    window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # Dark Style Theme
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(window.exec_())

