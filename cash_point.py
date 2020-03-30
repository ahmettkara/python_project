# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cash_point.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(750, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 110, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 110, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(150, 190, 541, 131))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 340, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 340, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(150, 410, 256, 101))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 420, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 410, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 410, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 40, 16, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(430, 50, 51, 31))
        self.spinBox.setAutoFillBackground(False)
        self.spinBox.setMaximum(99)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(530, 50, 161, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(700, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "                                                                         CASH SCREEN"))
        self.label.setText(_translate("MainWindow", "BARKOD:"))
        self.pushButton.setText(_translate("MainWindow", "EKLE"))
        self.pushButton_2.setText(_translate("MainWindow", "CIKAR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "URUN ADI:"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "BIRIM FIYAT:"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ADET/MIKTAR:"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "FIYAT:"))
        self.pushButton_4.setText(_translate("MainWindow", "HESAPLA"))
        self.pushButton_3.setText(_translate("MainWindow", "TEMIZLE"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                          "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:35pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                          "-qt-block-indent:0; text-indent:0px; font-family:\'MS "
                                                          "Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "SEPET:"))
        self.label_3.setText(_translate("MainWindow", "TUTAR:"))
        self.pushButton_5.setText(_translate("MainWindow", "ODEME"))
        self.pushButton_6.setText(_translate("MainWindow", "FIS YAZDIR"))
        self.label_4.setText(_translate("MainWindow", "X"))
        self.pushButton_7.setText(_translate("MainWindow", "CIKIS"))

####################################################################################################################
        self.pushButton.clicked.connect(self.add_basket) #sepete urun ekleme
        self.pushButton_2.clicked.connect(self.drop_product)  # sepetten urun cıkarma.
        self.pushButton_4.clicked.connect(self.calculate) # toplama
        self.pushButton_5.clicked.connect(self.cash_payment) #kasa odeme database update etme
        self.pushButton_6.clicked.connect(self.write_receipt) #fis ver ekranı sil
        self.pushButton_3.clicked.connect(self.clean_basket) #sepeti temizle
        self.pushButton_7.clicked.connect(self.get_to_login_screen) #giris ekranına geri don


####################################################################################################################
    barkod_liste=[]

    def add_basket(self):
        self.statusbar.showMessage("")
        self.db_baglan_01 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_01 = self.db_baglan_01.cursor()

        self.imlec_01.execute("SELECT * FROM barcode_table")
        secilen_01 = self.imlec_01.fetchall()

        barkod_numarasi_01 = self.lineEdit.text()

        barkod_numaralari_01 = []
        for i in secilen_01:
            barkod_numaralari_01 += [i[1]]

        if int(barkod_numarasi_01) in barkod_numaralari_01:
            for i in secilen_01:
                if i[1] == int(barkod_numarasi_01):
                    urun_adi_01 = i[2]
                    urun_fiyati_01 = i[5]
                    urun_miktari_01 = self.spinBox.value()

        Ui_MainWindow_3.barkod_liste += [[int(barkod_numarasi_01), urun_miktari_01]]

        table_01 = []
        table_02 = []
        table_01.append(urun_adi_01)
        table_01.append(float(urun_fiyati_01))
        table_01.append(urun_miktari_01)
        table_01.append(float(urun_fiyati_01) * urun_miktari_01)
        table_01 = tuple(table_01)
        table_02.append(table_01)

        self.tableWidget.insertRow(0)
        for row, form in enumerate(table_02):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
                column += 1
            row_position=self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

        self.lineEdit.setText("")
        self.spinBox.setValue(1)

##################################################################################################################
    def calculate(self):
        number_rows = self.tableWidget.rowCount() / 2
        payment = 0

        for i in range(int(number_rows)):

            urun_adi_03 = self.tableWidget.item(i, 0).text()
            urun_miktari_03 = self.tableWidget.item(i, 2).text()

            if urun_miktari_03 == "3" and " #1" in urun_adi_03:                      #UC AL BIR ODE VARSA
                pay = float(self.tableWidget.item(i, 3).text())/3
                payment += pay

            elif urun_miktari_03 == "2" and " #2" in urun_adi_03:                   #IKINCISI YARI FIYATINA VARSA
                pay = float(self.tableWidget.item(i, 3).text()) / 4 * 3
                payment += pay

            else:                                                                   #URUNDE KAMPANYA YOKSA
                pay = float(self.tableWidget.item(i, 3).text()) #int degil float yapınca duzeldi.
                payment += pay

        payment = round(payment,2)
        self.textBrowser.setText(str(payment))


##################################################################################################################
    def cash_payment(self):

        #print(Ui_MainWindow_3.barkod_liste)
        self.db_baglan_02 = sqlite3.connect("market_veri_tabani.db")
        self.imlec_02 = self.db_baglan_02.cursor()

        self.imlec_02.execute("SELECT * FROM barcode_table")
        secilen_02 = self.imlec_02.fetchall()

        for i in Ui_MainWindow_3.barkod_liste:
            self.imlec_02.execute("UPDATE barcode_table SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
            self.db_baglan_02.commit()

            for j in secilen_02:
                if i[0] in j:
                    urun_kategorisi_02 = j[0]


            if urun_kategorisi_02 == "DONDURULMUS GIDA":
                self.imlec_02.execute("UPDATE dondurulmus_gida SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "KONSERVELER":
                self.imlec_02.execute("UPDATE konserveler SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "KURU GIDALAR":
                self.imlec_02.execute("UPDATE kuru_gidalar SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "MESRUBAT":
                self.imlec_02.execute("UPDATE mesrubat SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "SARKUTERI":
                self.imlec_02.execute("UPDATE sarkuteri SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "SEBZE VE MEYVELER":
                self.imlec_02.execute("UPDATE sebze_meyve SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "SUT URUNLERI":
                self.imlec_02.execute("UPDATE sut_urunleri SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "TEMIZLIK URUNLERI":
                self.imlec_02.execute("UPDATE temizlik_urunleri SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "UNLU MAMULLER":
                self.imlec_02.execute("UPDATE unlu_mamuller SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "ATISTIRMALIKLAR":
                self.imlec_02.execute("UPDATE atistirmaliklar SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

            elif urun_kategorisi_02 == "EV GERECLERI":
                self.imlec_02.execute("UPDATE ev_gerecleri SET urun_miktari=urun_miktari-?  WHERE barkod=?", (i[1], i[0]))
                self.db_baglan_02.commit()

        Ui_MainWindow_3.barkod_liste.clear()
        #print(Ui_MainWindow_3.barkod_liste)
        self.statusbar.showMessage("VERI TABANI BASARIYLA GUNCELLENDI...")


####################################################################################################################
    def write_receipt(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        self.textBrowser.setText("")
        self.statusbar.showMessage("")

####################################################################################################################
    def drop_product(self):
        urun_satiri = self.lineEdit.text()
        self.tableWidget.removeRow(int(urun_satiri)-1) #0'dan basladıgı icin -1 yapıyorum.
        self.statusbar.showMessage("URUN BASARIYLA CIKARILDI...")

####################################################################################################################
    def clean_basket(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        self.textBrowser.setText("")

####################################################################################################################
    def get_to_login_screen(self):

        quit()
        # from stock.login_screen import Ui_MainWindow_1
        # self.ui_1 = Ui_MainWindow_1()
        # self.ui_1.setupUi(MainWindow)
        #ANA EKRANA GECISTE SIMDILIK SIKINTI VAR.

####################################################################################################################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





