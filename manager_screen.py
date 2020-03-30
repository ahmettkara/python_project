# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(750, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.tabWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.tabWidget.setMaximumSize(QtCore.QSize(800, 600))
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 431, 431))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(470, 200, 251, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 20, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 270, 251, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 340, 251, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(470, 410, 251, 51))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(470, 20, 111, 41))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setGeometry(QtCore.QRect(470, 100, 161, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(470, 80, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget)
        self.pushButton_13.setGeometry(QtCore.QRect(640, 80, 81, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(470, 20, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(470, 40, 161, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(470, 140, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setGeometry(QtCore.QRect(470, 160, 161, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget)
        self.pushButton_14.setGeometry(QtCore.QRect(640, 140, 81, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(200, 30, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(200, 80, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(30, 270, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setGeometry(QtCore.QRect(200, 280, 211, 31))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(500) ###############################################################
        self.spinBox.setProperty("value", 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 230, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit.setGeometry(QtCore.QRect(200, 330, 211, 31))
        self.dateEdit.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(480, 80, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(480, 280, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(30, 170, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(200, 180, 211, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(200, 130, 211, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_17.setGeometry(QtCore.QRect(480, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_18.setGeometry(QtCore.QRect(480, 330, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(480, 130, 211, 131))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(420, 40, 51, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_21 = QtWidgets.QLabel(self.tab_7)
        self.label_21.setGeometry(QtCore.QRect(50, 140, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_7)
        self.label_22.setGeometry(QtCore.QRect(50, 20, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_4.setGeometry(QtCore.QRect(50, 70, 671, 51))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_14.setGeometry(QtCore.QRect(50, 210, 671, 41))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 290, 191, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 290, 191, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_7)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 370, 671, 121))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_16.setGeometry(QtCore.QRect(290, 290, 191, 51))
        self.pushButton_16.setObjectName("pushButton_16")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 30, 211, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(30, 70, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 120, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(30, 170, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(30, 220, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(30, 270, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 80, 211, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 130, 211, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 180, 211, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 230, 211, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(190, 280, 211, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(480, 30, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setDefault(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(480, 80, 211, 331))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(190, 440, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setGeometry(QtCore.QRect(310, 440, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(30, 320, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(190, 330, 211, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(30, 370, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_12.setGeometry(QtCore.QRect(190, 380, 211, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab)
        self.pushButton_15.setGeometry(QtCore.QRect(480, 440, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(410, 40, 51, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "                                                           MANAGER SCREEN"))
        self.pushButton.setText(_translate("MainWindow", "TUM MALLARI SORGULA"))
        self.pushButton_2.setText(_translate("MainWindow", "SORGULA"))
        self.pushButton_5.setText(_translate("MainWindow", "KAMPANYALI URUNLERI SORGULA"))
        self.pushButton_6.setText(_translate("MainWindow", "SON KULLANMA TARIHI SORGULA"))
        self.pushButton_9.setText(_translate("MainWindow", "TUKENEN VE AZALANLARI SORGULA"))
        self.label_15.setText(_translate("MainWindow", "URUN ADI:"))
        self.pushButton_13.setText(_translate("MainWindow", "SORGULA"))
        self.label_16.setText(_translate("MainWindow", "URUN KATEGORISI:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "SEBZE VE MEYVELER"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "UNLU MAMULLER"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "SARKUTERI"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "DONDURULMUS GIDA"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "SUT URUNLERI"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "MESRUBAT"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "ATISTIRMALIKLAR"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "KONSERVELER"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "KURU GIDALAR"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "TEMIZLIK URUNLERI"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "EV GERECLERI"))
        self.label_17.setText(_translate("MainWindow", "URUN MARKASI:"))
        self.pushButton_14.setText(_translate("MainWindow", "SORGULA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "INVENTORY"))
        self.label.setText(_translate("MainWindow", "BARKOD NUMARASI:"))
        self.label_2.setText(_translate("MainWindow", "URUN KATEGORISI:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "SEBZE VE MEYVELER"))
        self.comboBox.setItemText(1, _translate("MainWindow", "UNLU MAMULLER"))
        self.comboBox.setItemText(2, _translate("MainWindow", "SARKUTERI"))
        self.comboBox.setItemText(3, _translate("MainWindow", "DONDURULMUS GIDA"))
        self.comboBox.setItemText(4, _translate("MainWindow", "SUT URUNLERI"))
        self.comboBox.setItemText(5, _translate("MainWindow", "MESRUBAT"))
        self.comboBox.setItemText(6, _translate("MainWindow", "ATISTIRMALIKLAR"))
        self.comboBox.setItemText(7, _translate("MainWindow", "KONSERVELER"))
        self.comboBox.setItemText(8, _translate("MainWindow", "KURU GIDALAR"))
        self.comboBox.setItemText(9, _translate("MainWindow", "TEMIZLIK URUNLERI"))
        self.comboBox.setItemText(10, _translate("MainWindow", "EV GERECLERI"))
        self.label_3.setText(_translate("MainWindow", "URUN ADI:"))
        self.label_4.setText(_translate("MainWindow", "URUN BIRIM FIYATI:"))
        self.label_5.setText(_translate("MainWindow", "URUN ADEDI/MIKTARI:"))
        self.label_6.setText(_translate("MainWindow", "SON KULLANMA TARIHI:"))
        self.pushButton_7.setText(_translate("MainWindow", "GUNCELLE"))
        self.pushButton_8.setText(_translate("MainWindow", "EKLE"))
        self.label_20.setText(_translate("MainWindow", "URUN MARKASI:"))
        self.pushButton_17.setText(_translate("MainWindow", "SORGULA"))
        self.pushButton_18.setText(_translate("MainWindow", "CIKAR"))
        self.label_23.setText(_translate("MainWindow", "--->>>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ADD/DROP"))
        self.label_21.setText(_translate("MainWindow", "KAMPANYANIN UYGULANACAGI URUNUN BARKOD NUMARASINI GIRINIZ:"))
        self.label_22.setText(_translate("MainWindow", "UYGULAMAK ISTEDIGINIZ KAMPANYAYI SECINIZ:"))
        self.comboBox_4.setCurrentText(_translate("MainWindow", "Hicbiri..."))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Hicbiri..."))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "100 EURO VE UZERI HARCAMALARDA %10 INDIRIM KAMPANYASI"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "IKINCI URUN YARI FIYATINA KAMPANYASI"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "UC AL BIR ODE KAMPANYASI"))
        self.pushButton_3.setText(_translate("MainWindow", "URUN BILGISI GOSTER"))
        self.pushButton_4.setText(_translate("MainWindow", "KAMPANYAYI BITIR"))
        self.pushButton_16.setText(_translate("MainWindow", "KAMPANYAYI BASLAT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "CAMPAING"))
        self.label_7.setText(_translate("MainWindow", "SICIL NUMARASI:"))
        self.label_8.setText(_translate("MainWindow", "SIFRESI:"))
        self.label_9.setText(_translate("MainWindow", "ADI SOYADI:"))
        self.label_10.setText(_translate("MainWindow", "GOREVI:"))
        self.label_11.setText(_translate("MainWindow", "BASLAMA TARIHI:"))
        self.label_12.setText(_translate("MainWindow", "MAASI:"))
        self.pushButton_10.setText(_translate("MainWindow", "PERSONELI SORGULA"))
        self.pushButton_11.setText(_translate("MainWindow", "KAYDET"))
        self.pushButton_12.setText(_translate("MainWindow", "SIL"))
        self.label_13.setText(_translate("MainWindow", "CALISMA SAATLERI:"))
        self.label_18.setText(_translate("MainWindow", "FAZLA MESAI:"))
        self.pushButton_15.setText(_translate("MainWindow", "TUM PERSONELI GOSTER"))
        self.label_19.setText(_translate("MainWindow", "--->>>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "PERSONEL"))

####################################################################################################################
        self.pushButton_10.clicked.connect(self.personel_query) # sicil numarası ile personel sorgulama
        self.pushButton_15.clicked.connect(self.all_personel) # tum personeli gosterme
        self.pushButton_11.clicked.connect(self.personel_save) # personel ekleme
        self.pushButton_12.clicked.connect(self.personel_delete) # personel silme
        self.pushButton_17.clicked.connect(self.barcode_query) #urun barkodu sorgulama
        self.pushButton_7.clicked.connect(self.product_update)  # urun bılgılerı guncelleme
        self.pushButton_8.clicked.connect(self.product_add) #yeni urun ekleme
        self.pushButton_18.clicked.connect(self.product_drop) #urun cikarma
        self.pushButton.clicked.connect(self.all_product_query) #tum urunleri sorgulama
        self.pushButton_6.clicked.connect(self.expire_date) #son kullanma tarihi gelenleri sorgulama
        self.pushButton_9.clicked.connect(self.decreasing) # azalan urunleri sorgulama
        self.pushButton_2.clicked.connect(self.category_product_query) #urunleri kategoriye gore sorgulama
        self.pushButton_13.clicked.connect(self.product_name_query) # urunleri isme gore sorgulama
        self.pushButton_14.clicked.connect(self.product_brand_query) #urunleri markalarına gore sorgulama
        self.pushButton_16.clicked.connect(self.start_campaing) #kampanya baslatma
        self.pushButton_4.clicked.connect(self.end_campaing) # kampanya bitirme
        self.pushButton_3.clicked.connect(self.campaing_product_query) #kampanya ekranında urun bilgisi sorgulama
        self.pushButton_5.clicked.connect(self.campaing_query) # kampanyalı urunleri sorgulama

####################################################################################################################
    def personel_query(self):
        self.textBrowser_2.setText("")
        self.db_baglan = sqlite3.connect("market_veri_tabani.db")
        self.imlec = self.db_baglan.cursor()
        self.imlec.execute("SELECT * FROM personel_table")
        secilen = self.imlec.fetchall()
        #print(secilen)
        sicil_numarasi = self.lineEdit_3.text()

        sayac = 1
        for i in secilen:
            if sicil_numarasi == str(i[0]):
                self.lineEdit_4.setText(str(i[1]))
                self.lineEdit_5.setText(str(i[2]))
                self.lineEdit_6.setText(str(i[3]))
                self.lineEdit_7.setText(str(i[4]))
                self.lineEdit_8.setText(str(i[5]))
                self.lineEdit_9.setText(str(i[6]))
                self.lineEdit_12.setText(str(i[7]))
                break

            if sayac == (len(secilen)):
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
                self.lineEdit_6.setText("")
                self.lineEdit_7.setText("")
                self.lineEdit_8.setText("")
                self.lineEdit_9.setText("")
                self.lineEdit_12.setText("")
                self.textBrowser_2.setText("KAYIT BULUNAMADI")

            sayac += 1

####################################################################################################################
    def all_personel(self):
        self.db_baglan_2 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_2 = self.db_baglan_2.cursor()
        self.imlec_2.execute("SELECT * FROM personel_table")
        secilen_2 = self.imlec_2.fetchall()
        #print(secilen_2)

        personeller = ""
        for i in secilen_2:
            personeller += str(i[0]) + " --> " + str(i[2]) + "\n"
        self.textBrowser_2.setText(personeller)

####################################################################################################################
    def personel_save(self):
        self.db_baglan_3 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_3 = self.db_baglan_3.cursor()
        self.imlec_3.execute("SELECT * FROM personel_table")
        secilen_3 = self.imlec_3.fetchall()

        sicil_numaralari = []
        for i in secilen_3:
            sicil_numaralari.append(i[0])

        sicil_numarasi_3 = self.lineEdit_3.text()
        sifresi_3 = self.lineEdit_4.text()
        adi_soyadi_3 = self.lineEdit_5.text()
        gorevi_3 = self.lineEdit_6.text()
        baslama_tarihi_3 = self.lineEdit_7.text()
        maasi_3 = self.lineEdit_8.text()
        calisma_saatleri_3 = self.lineEdit_9.text()
        fazla_mesai_3 = self.lineEdit_12.text()

        if int(sicil_numarasi_3) in sicil_numaralari:

            self.imlec_3.execute(
                "UPDATE personel_table SET sifresi=?, adi_soyadi=?, gorevi=?, baslama_tarihi=?, maasi=?, "
                "calisma_saatleri=?, fazla_mesai=? WHERE sicil_numarasi=?",
                (int(sifresi_3), adi_soyadi_3, gorevi_3, baslama_tarihi_3, int(maasi_3), calisma_saatleri_3,
                 int(fazla_mesai_3), int(sicil_numarasi_3)))
            self.imlec_3.execute("UPDATE login_table SET password=?, personel_position=? WHERE registration_no=?",
                                 (int(sifresi_3), gorevi_3, int(sicil_numarasi_3)))
            self.db_baglan_3.commit()

            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("")
            self.lineEdit_12.setText("")
            self.textBrowser_2.setText("PERSONEL BILGILERI GUNCELLENDI")

        else:
            self.imlec_3.execute("INSERT INTO personel_table VALUES (?,?,?,?,?,?,?,?)", (
            int(sicil_numarasi_3), int(sifresi_3), adi_soyadi_3, gorevi_3, baslama_tarihi_3, int(maasi_3),
            calisma_saatleri_3, int(fazla_mesai_3)))
            self.imlec_3.execute("INSERT INTO login_table VALUES (?,?,?)",
                                 (int(sicil_numarasi_3), int(sifresi_3), gorevi_3))
            self.db_baglan_3.commit()

            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("")
            self.lineEdit_12.setText("")
            self.textBrowser_2.setText("YENI PERSONEL EKLENDI")

####################################################################################################################
    def personel_delete(self):
        self.textBrowser_2.setText("")
        self.db_baglan_4 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_4 = self.db_baglan_4.cursor()

        self.imlec_4.execute("SELECT * FROM personel_table")
        secilen_4 = self.imlec_4.fetchall()

        sicil_numarasi_4 = self.lineEdit_3.text()

        self.imlec_4.execute("DELETE FROM personel_table WHERE sicil_numarasi=?", (int(sicil_numarasi_4),))
        self.imlec_4.execute("DELETE FROM login_table WHERE registration_no=?", (int(sicil_numarasi_4),))
        self.db_baglan_4.commit()

        self.textBrowser_2.setText("PERSONEL SILINDI")


####################################################################################################################
    def barcode_query(self):
        self.textBrowser_4.setText("")
        self.db_baglan_5 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_5 = self.db_baglan_5.cursor()
        self.imlec_5.execute("SELECT * FROM barcode_table")
        secilen_5 = self.imlec_5.fetchall()
        #print(secilen_5)

        barkod_numaralari=[]
        for i in secilen_5:
            barkod_numaralari += [i[1]]
        #print(barkod_numaralari)

        barkod_numarasi=self.lineEdit.text()

        if int(barkod_numarasi) in barkod_numaralari:
            for i in secilen_5:
                if int(barkod_numarasi)==i[1]:
                    self.comboBox.setCurrentText(str(i[0]))
                    self.lineEdit_15.setText(str(i[2]))
                    self.lineEdit_13.setText(str(i[3]))
                    self.spinBox.setValue(i[4])
                    self.lineEdit_2.setText(str(i[5]))
                    tarih=i[6]
                    tarih_bol=tarih.split("-")
                    #print(tarih_bol)
                    gun = int(tarih_bol[2])
                    ay = int(tarih_bol[1])
                    yil = int(tarih_bol[0])
                    self.dateEdit.setDate(QDate(yil, ay, gun))

        else:
            self.textBrowser_4.setText("\n\n\n          KAYIT BULUNAMADI")
            self.lineEdit_15.setText("")
            self.lineEdit_13.setText("")
            self.spinBox.setValue(0)
            self.lineEdit_2.setText("")
            #tarihi sıfırlamıyor şimdilik.


####################################################################################################################
    def product_update(self):

        self.db_baglan_6 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_6 = self.db_baglan_6.cursor()
        self.imlec_6.execute("SELECT * FROM barcode_table")
        secilen_6 = self.imlec_6.fetchall()
        #print(secilen_6)

        barkod_numaralari_6=[]
        for i in secilen_6:
            barkod_numaralari_6 += [i[1]]
        #print(barkod_numaralari_6)

        barkod_numarasi_6=self.lineEdit.text()
        urun_kategorisi_6 = self.comboBox.currentText()
        urun_adi_6 = self.lineEdit_15.text()
        urun_markasi_6 = self.lineEdit_13.text()
        urun_fiyati_6 = self.lineEdit_2.text()
        urun_miktari_6 = self.spinBox.value()
        # SON KULLANMA TARIHLERINI SONRADAN EKLEDIGIM ICIN BU SAYFADA TARIH SIMDILIK GUNCELLENMIYOR. EKLENECEK.

        if int(barkod_numarasi_6) in barkod_numaralari_6:

            self.imlec_6.execute(
                "UPDATE barcode_table SET urun_kategorisi=?, urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                "urun_miktari=?  WHERE barkod=?",
                (urun_kategorisi_6, urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
            self.db_baglan_6.commit()

            if urun_kategorisi_6 == "DONDURULMUS GIDA":
                self.imlec_6.execute("UPDATE dondurulmus_gida SET urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                                     "urun_miktari=?  WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6), int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("DONDURULMUS GIDA GUNCELLENDI.")

            elif urun_kategorisi_6 == "KONSERVELER":
                self.imlec_6.execute("UPDATE konserveler SET urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                                     "urun_miktari=?  WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("KONSERVE GUNCELLENDI")

            elif urun_kategorisi_6 == "KURU GIDALAR":
                self.imlec_6.execute("UPDATE kuru_gidalar SET urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                                     "urun_miktari=?  WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("KURU GIDA GUNCELLENDI")

            elif urun_kategorisi_6 == "MESRUBAT":
                self.imlec_6.execute("UPDATE mesrubat SET urun_adi=?, urun_markasi=?, urun_fiyati=?, urun_miktari=?  "
                                     "WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("MESRUBAT GUNCELLENDI")

            elif urun_kategorisi_6 == "SARKUTERI":
                self.imlec_6.execute("UPDATE sarkuteri SET urun_adi=?, urun_markasi=?, urun_fiyati=?, urun_miktari=?  "
                                     "WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("SARKUTERI GUNCELLENDI")

            elif urun_kategorisi_6 == "SEBZE VE MEYVELER":
                self.imlec_6.execute("UPDATE sebze_meyve SET urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                                     "urun_miktari=?  WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("SEBZE VE MEYVELER GUNCELLENDI")

            elif urun_kategorisi_6 == "SUT URUNLERI":
                self.imlec_6.execute("UPDATE sut_urunleri SET urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                                     "urun_miktari=?  WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("SUT URUNU GUNCELLENDI")

            elif urun_kategorisi_6 == "TEMIZLIK URUNLERI":
                self.imlec_6.execute("UPDATE temizlik_urunleri SET urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                                     "urun_miktari=?  WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("TEMIZLIK URUNU GUNCELLENDI")

            elif urun_kategorisi_6 == "UNLU MAMULLER":
                self.imlec_6.execute("UPDATE unlu_mamuller SET urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                                     "urun_miktari=?  WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("UNLU MAMULLER GUNCELLENDI")

            elif urun_kategorisi_6 == "ATISTIRMALIKLAR":
                self.imlec_6.execute("UPDATE atistirmaliklar SET urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                                     "urun_miktari=?  WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("ATISTIRMALIKLAR GUNCELLENDI")

            elif urun_kategorisi_6 == "EV GERECLERI":
                self.imlec_6.execute("UPDATE ev_gerecleri SET urun_adi=?, urun_markasi=?, urun_fiyati=?, "
                                     "urun_miktari=?  WHERE barkod=?",
                                     (urun_adi_6, urun_markasi_6, urun_fiyati_6, int(urun_miktari_6),int(barkod_numarasi_6)))
                self.db_baglan_6.commit()
                self.textBrowser_4.setText("EV GERECLERI GUNCELLENDI")


####################################################################################################################
    def product_add(self):
        self.db_baglan_7 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_7 = self.db_baglan_7.cursor()
        self.imlec_7.execute("SELECT * FROM barcode_table")
        secilen_7 = self.imlec_7.fetchall()

        barkod_numaralari_7=[]
        for i in secilen_7:
            barkod_numaralari_7 += [i[1]]

        barkod_numarasi_7 = self.lineEdit.text()
        urun_kategorisi_7 = self.comboBox.currentText()
        urun_adi_7 = self.lineEdit_15.text()
        urun_markasi_7 = self.lineEdit_13.text()
        urun_fiyati_7 = self.lineEdit_2.text()
        urun_miktari_7 = self.spinBox.value()
        son_kullanma_tarihi_7=self.dateEdit.date().toPyDate()

        # print(son_kullanma_tarihi_7) #bu sekilde donuyor PyQt5.QtCore.QDate(2020, 1, 1)
        # print(type(son_kullanma_tarihi_7)) #<class 'datetime.date'>

        if int(barkod_numarasi_7) not in barkod_numaralari_7:

            self.imlec_7.execute(
                "INSERT INTO barcode_table VALUES (?,?,?,?,?,?,?)",
                (urun_kategorisi_7, int(barkod_numarasi_7), urun_adi_7, urun_markasi_7,  int(urun_miktari_7), urun_fiyati_7,son_kullanma_tarihi_7))
            self.db_baglan_7.commit()

            if urun_kategorisi_7 == "DONDURULMUS GIDA":
                self.imlec_7.execute("INSERT INTO dondurulmus_gida VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7), urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("DONDURULMUS GIDA EKLENDI")

            elif urun_kategorisi_7 == "KONSERVELER":
                self.imlec_7.execute("INSERT INTO konserveler VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("KONSERVELER EKLENDI")

            elif urun_kategorisi_7 == "KURU GIDALAR":
                self.imlec_7.execute("INSERT INTO kuru_gidalar VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("KURU GIDALAR EKLENDI")

            elif urun_kategorisi_7 == "MESRUBAT":
                self.imlec_7.execute("INSERT INTO mesrubat VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("MESRUBAT EKLENDI")

            elif urun_kategorisi_7 == "SARKUTERI":
                self.imlec_7.execute("INSERT INTO sarkuteri VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("SARKUTERI EKLENDI")

            elif urun_kategorisi_7 == "SEBZE VE MEYVELER":
                self.imlec_7.execute("INSERT INTO sebze_meyve VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("SEBZE VE MEYVELER EKLENDI")

            elif urun_kategorisi_7 == "SUT URUNLERI":
                self.imlec_7.execute("INSERT INTO sut_urunleri VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("SUT URUNLERI EKLENDI")

            elif urun_kategorisi_7 == "TEMIZLIK URUNLERI":
                self.imlec_7.execute("INSERT INTO temizlik_urunleri VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("TEMIZLIK URUNLERI EKLENDI")

            elif urun_kategorisi_7 == "UNLU MAMULLER":
                self.imlec_7.execute("INSERT INTO unlu_mamuller VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("UNLU MAMULLER EKLENDI")

            elif urun_kategorisi_7 == "ATISTIRMALIKLAR":
                self.imlec_7.execute("INSERT INTO atistirmaliklar VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("ATISTIRMALIKLAR EKLENDI")

            elif urun_kategorisi_7 == "EV GERECLERI":
                self.imlec_7.execute("INSERT INTO ev_gerecleri VALUES (?,?,?,?,?,?)",
                                     (int(barkod_numarasi_7), urun_adi_7, urun_markasi_7, int(urun_miktari_7),
                                      urun_fiyati_7, son_kullanma_tarihi_7))
                self.db_baglan_7.commit()
                self.textBrowser_4.setText("EV GERECLERI EKLENDI")


####################################################################################################################
    def product_drop(self):

        self.textBrowser_4.setText("")
        self.db_baglan_8 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_8 = self.db_baglan_8.cursor()

        barkod_numarasi_8 = self.lineEdit.text()
        urun_kategorisi_8 = self.comboBox.currentText()

        self.imlec_8.execute("DELETE FROM barcode_table WHERE barkod=?", (int(barkod_numarasi_8),))
        self.db_baglan_8.commit()

        if urun_kategorisi_8 == "DONDURULMUS GIDA":
            self.imlec_8.execute("DELETE FROM dondurulmus_gida WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("DONDURULMUS GIDA SILINDI")

        elif urun_kategorisi_8 == "KONSERVELER":
            self.imlec_8.execute("DELETE FROM konserveler WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("KONSERVE SILINDI ")

        elif urun_kategorisi_8 == "KURU GIDALAR":
            self.imlec_8.execute("DELETE FROM kuru_gidalar WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("KURU GIDA SILINDI")

        elif urun_kategorisi_8 == "MESRUBAT":
            self.imlec_8.execute("DELETE FROM mesrubat WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("MESRUBAT SILINDI")

        elif urun_kategorisi_8 == "SARKUTERI":
            self.imlec_8.execute("DELETE FROM sarkuteri WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("SARKUTERI SILINDI")

        elif urun_kategorisi_8 == "SEBZE VE MEYVELER":
            self.imlec_8.execute("DELETE FROM sebze_meyve WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("SEBZE MEYVE SILINDI")

        elif urun_kategorisi_8 == "SUT URUNLERI":
            self.imlec_8.execute("DELETE FROM sut_urunleri WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("SUT URUNU SILINDI")

        elif urun_kategorisi_8 == "TEMIZLIK URUNLERI":
            self.imlec_8.execute("DELETE FROM temizlik_urunleri WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("TEMIZLIK URUNU SILINDI")

        elif urun_kategorisi_8 == "UNLU MAMULLER":
            self.imlec_8.execute("DELETE FROM unlu_mamuller WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("UNLU MAMUL SILINDI")

        elif urun_kategorisi_8 == "ATISTIRMALIKLAR":
            self.imlec_8.execute("DELETE FROM atistirmaliklar WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("ATISTIRMALIK SILINDI")

        elif urun_kategorisi_8 == "EV GERECLERI":
            self.imlec_8.execute("DELETE FROM ev_gerecleri WHERE barkod=?", (int(barkod_numarasi_8),))
            self.db_baglan_8.commit()
            self.textBrowser_4.setText("EV GERECİ SILINDI")


############################################################################################################
############################################################################################################
    def all_product_query(self):

        self.db_baglan_9 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_9 = self.db_baglan_9.cursor()
        self.imlec_9.execute("SELECT * FROM barcode_table")
        secilen_9 = self.imlec_9.fetchall()
        text_9 = ""
        for count, i in enumerate(secilen_9,1):
            text_9 += str(count) + ")" + " --- " + str(i[1]) + " --- " + i[3] + " --- " + i[2] + "\n"

        self.textBrowser.setText(text_9)


############################################################################################################
    def expire_date(self):

        self.db_baglan_10 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_10 = self.db_baglan_10.cursor()
        self.imlec_10.execute("SELECT * FROM barcode_table")
        secilen_10 = self.imlec_10.fetchall()
        skt_hepsi = [i[6] for i in secilen_10]
        skt_az = []
        for i in skt_hepsi:
            tar = i.split("-")
            y=int(tar[0])
            a=int(tar[1])
            g=int(tar[2])

            now = QDate.currentDate()
            exp = QDate(y,a,g)
            dif = now.daysTo(exp)

            if dif < 30:
                skt_az.append(i)

        text_10 = "TARIH: " + str(QDate.currentDate().toPyDate()) + "\n" + "\n" + \
                  "UYARI! ASAGIDAKI URUNLERIN SON KULLANMA TARİHİNE 30 GUNDEN AZ KALMISTIR!:" + "\n" + "\n"

        for i in secilen_10:
            if i[6] in skt_az:
                text_10 += "BARKOD:  " + str(i[1]) + "     SKT:  " + i[6] + "     URUN:  " + i[2] + "\n"

        self.textBrowser.setText(text_10)


############################################################################################################
    def decreasing(self):

        self.db_baglan_11 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_11 = self.db_baglan_11.cursor()
        self.imlec_11.execute("SELECT * FROM barcode_table")
        secilen_11 = self.imlec_11.fetchall()

        dec = [i[4] for i in secilen_11 if i[4] < 50]

        text_11 = "UYARI! ASAGIDAKI URUNLER, STOKTA 50 ADETTEN AZ KALMISTIR! \n\n"
        for i in secilen_11:
            if i[4] in dec:
                text_11 += "BARKOD:  " + str(i[1]) + "     ADET:  " + str(i[4]) + "     URUN:  " + i[2] +  "\n"

        self.textBrowser.setText(text_11)



############################################################################################################
    def category_product_query(self):

        self.db_baglan_12 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_12 = self.db_baglan_12.cursor()
        urun_kategorisi_12 = self.comboBox_3.currentText()

        if urun_kategorisi_12 == "DONDURULMUS GIDA":
            self.imlec_12.execute("SELECT * FROM dondurulmus_gida")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN DONDURULMUS GIDALAR:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "KONSERVELER":
            self.imlec_12.execute("SELECT * FROM konserveler")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN KONSERVELER:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "KURU GIDALAR":
            self.imlec_12.execute("SELECT * FROM kuru_gidalar")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN KURU GIDALAR:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "MESRUBAT":
            self.imlec_12.execute("SELECT * FROM mesrubat")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN MESRUBATLAR:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "SARKUTERI":
            self.imlec_12.execute("SELECT * FROM sarkuteri")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN ET URUNLERI:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "SEBZE VE MEYVELER":
            self.imlec_12.execute("SELECT * FROM sebze_meyve")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN SEBZE VE MEYVELER:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "SUT URUNLERI":
            self.imlec_12.execute("SELECT * FROM sut_urunleri")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN SUT URUNLERI:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "TEMIZLIK URUNLERI":
            self.imlec_12.execute("SELECT * FROM temizlik_urunleri")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN TEMIZLIK URUNLERI:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "UNLU MAMULLER":
            self.imlec_12.execute("SELECT * FROM unlu_mamuller")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN UNLU MAMULLER:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "EV GERECLERI":
            self.imlec_12.execute("SELECT * FROM ev_gerecleri")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN EV GERECLERI:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)

        elif urun_kategorisi_12 == "ATISTIRMALIKLAR":
            self.imlec_12.execute("SELECT * FROM atistirmaliklar")
            secilen_12 = self.imlec_12.fetchall()
            text_12 = "STOKTA BULUNAN ATISTIRMALIKLAR:\n\n"
            for i in secilen_12:
                text_12 += "BARKOD: " + str(i[0]) + "     " + i[2] + "--" + i[1] + "\n"
            self.textBrowser.setText(text_12)



############################################################################################################
    def product_name_query(self):
        self.db_baglan_13 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_13 = self.db_baglan_13.cursor()
        self.imlec_13.execute("SELECT * FROM barcode_table")
        secilen_13 = self.imlec_13.fetchall()
        product_name = self.lineEdit_10.text().upper().rstrip()
        text_13 = ""
        for i in secilen_13:
            if product_name in i:
                text_13 += "BARKOD:  " + str(i[1]) + "     " + i[3] + "--" + i[2] + "\n"
        self.textBrowser.setText(text_13)
        self.lineEdit_10.setText("")

    ############################################################################################################
    def product_brand_query(self):
        self.db_baglan_14 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_14 = self.db_baglan_14.cursor()
        self.imlec_14.execute("SELECT * FROM barcode_table")
        secilen_14 = self.imlec_14.fetchall()
        brand_name = self.lineEdit_11.text().upper().rstrip()
        text_14 = ""
        for i in secilen_14:
            if brand_name in i:
                text_14 += "BARKOD:  " + str(i[1]) + "     " + i[3] + "--" + i[2] + "\n"
        self.textBrowser.setText(text_14)
        self.lineEdit_11.setText("")


############################################################################################################
    def start_campaing(self):
        self.db_baglan_15 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_15 = self.db_baglan_15.cursor()
        self.imlec_15.execute("SELECT * FROM barcode_table")
        secilen_15 = self.imlec_15.fetchall()
        camp_name_15 = self.comboBox_4.currentText()
        barkod_15 = self.lineEdit_14.text()

        if camp_name_15 == "UC AL BIR ODE KAMPANYASI":

            for i in secilen_15:
                if i[1] == int(barkod_15):
                    urun_adi_15 = i[2]+" #1"
                    self.imlec_15.execute("UPDATE barcode_table SET urun_adi=? WHERE barkod=?",
                                          (urun_adi_15, int(barkod_15)))
                    self.db_baglan_15.commit()
                    self.textBrowser_3.setText("UC AL BIR ODE KAMPANYASI BASLATILDI. DATABASE GUNCELLENDI")
                    self.lineEdit_14.setText("")

        elif camp_name_15 == "IKINCI URUN YARI FIYATINA KAMPANYASI":

            for i in secilen_15:
                if i[1] == int(barkod_15):
                    urun_adi_15 = i[2]+" #2"
                    self.imlec_15.execute("UPDATE barcode_table SET urun_adi=? WHERE barkod=?",
                                          (urun_adi_15, int(barkod_15)))
                    self.db_baglan_15.commit()
                    self.textBrowser_3.setText("IKINCI URUN YARI FIYATINA KAMPANYASI BASLATILDI. DATABASE GUNCELLENDI")
                    self.lineEdit_14.setText("")


############################################################################################################
    def end_campaing(self):

        self.db_baglan_16 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_16 = self.db_baglan_16.cursor()
        self.imlec_16.execute("SELECT * FROM barcode_table")
        secilen_16 = self.imlec_16.fetchall()
        barkod_16 = self.lineEdit_14.text()

        for i in secilen_16:
            if i[1] == int(barkod_16) and " #1" in i[2]:
                urun_adi_16 = i[2][:-3:]
                self.imlec_16.execute("UPDATE barcode_table SET urun_adi=? WHERE barkod=?",
                                      (urun_adi_16, int(barkod_16)))
                self.db_baglan_16.commit()
                self.textBrowser_3.setText("UC AL BIR ODE KAMPANYASI BITIRILDI. DATABASE GUNCELLENDI")
                self.lineEdit_14.setText("")

            elif i[1] == int(barkod_16) and " #2" in i[2]:
                urun_adi_16 = i[2][:-3:]
                self.imlec_16.execute("UPDATE barcode_table SET urun_adi=? WHERE barkod=?",
                                      (urun_adi_16, int(barkod_16)))
                self.db_baglan_16.commit()
                self.textBrowser_3.setText("IKINCI URUN YARI FIYATINA KAMPANYASI BITIRILDI. DATABASE GUNCELLENDI")
                self.lineEdit_14.setText("")


############################################################################################################
    def campaing_product_query(self):

        self.db_baglan_17 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_17 = self.db_baglan_17.cursor()
        self.imlec_17.execute("SELECT * FROM barcode_table")
        secilen_17 = self.imlec_17.fetchall()
        barkod_17 = self.lineEdit_14.text()
        text_17 = ""
        for i in secilen_17:
            if i[1] == int(barkod_17):
                text_17 += "URUN:  " + i[2] + "     MARKA:  " + i[3] + "     ADET:  " + str(i[4]) + "     SKT:  " + i[6] + "\n"
        self.textBrowser_3.setText(text_17)


############################################################################################################
    def campaing_query(self):

        self.db_baglan_18 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_18 = self.db_baglan_18.cursor()
        self.imlec_18.execute("SELECT * FROM barcode_table")
        secilen_18 = self.imlec_18.fetchall()
        text_18 = ""
        for i in secilen_18:
            if " #1" in i[2]:
                text_18 += "BARKOD:  " + str(i[1]) + "      KAMPANYA:  UC AL BIR ODE" + "\n"

            elif " #2" in i[2]:
                text_18 += "BARKOD:  " + str(i[1]) + "      KAMPANYA:  IKINCI URUN YARI FIYATINA" + "\n"

        self.textBrowser.setText(text_18)
        if len(text_18) == 0:
            self.textBrowser.setText("KAMPANYALI URUN BULUNMAMAKTADIR!")

############################################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

