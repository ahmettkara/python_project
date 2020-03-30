# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random
from stock.manager_screen import Ui_MainWindow_2
from stock.cash_point import Ui_MainWindow_3


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QtCore.QSize(600, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 661, 511))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 80, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(250, 80, 251, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 150, 251, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(250, 290, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 360, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 220, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 220, 111, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(390, 220, 111, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
############################################################################################################
        self.robot_test() #giris ekranı her calıstıgında dogrulama kodu da degisecek.
############################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Login Screen"))
        self.label.setText(_translate("MainWindow", "Registration No:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "Sign in"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.label_4.setText(_translate("MainWindow", "Verifacation Code:"))

############################################################################################################
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.exit)

############################################################################################################
    def robot_test(self):
        not_robot = random.randrange(100, 1000)
        self.lineEdit_5.setText(str(not_robot))

############################################################################################################
    def exit(self):
        quit()

############################################################################################################
    def login(self):

        self.db_baglan = sqlite3.connect("market_veri_tabani.db")
        self.imlec = self.db_baglan.cursor()

        self.imlec.execute("Select * From login_table")
        secilen = self.imlec.fetchall()

        registration_no = self.lineEdit.text()
        password = self.lineEdit_3.text()
        verifacation_code = self.lineEdit_4.text()
        random_code = self.lineEdit_5.text()

        for i in secilen:
            if int(registration_no) == i[0] and int(password) == i[1] and int(random_code) == int(verifacation_code):

                if i[2] == "MANAGER":
                    self.ui = Ui_MainWindow_2()
                    self.ui.setupUi(MainWindow)

                elif i[2] == "CASHIER":
                    self.ui = Ui_MainWindow_3()
                    self.ui.setupUi(MainWindow)
                    self.imlec.execute("Select * From personel_table")
                    secilen_2 = self.imlec.fetchall()

                    for i in secilen_2:
                        if int(registration_no) == i[0]:
                            personel_adi = i[2]
                    self.ui.textBrowser_2.setText(personel_adi) #kasa ekranına personel adını yazdırma.

            else:
                self.statusbar.showMessage("HATALI GIRIS YAPTINIZ")
                self.robot_test()
                self.lineEdit.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")

############################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
