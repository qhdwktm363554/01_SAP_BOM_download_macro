# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\09.python\06.PYAUTOGUI_SAP_BOM_download\210716_introGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import bong
from bong import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(234, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 171, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.goto2nd)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def goto2nd(self):
        Ui_Bong()
        Ui_Bongsbongs.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hell_hard"))
        self.pushButton.setText(_translate("MainWindow", "START (To break, press F5)"))

class Ui_Bong(Ui_MainWindow):
    def __init__(self, parent = Ui_MainWindow):
        super().__init__()

    def setupUi_2(self, Ui_Bong):
        Ui_Bong.setObjectName("Ui_Bong")
        # QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.FramelessWindowHint
        Ui_Bong.resize(347, 241)
        Ui_Bongsbongs = QtWidgets.QWidget(Ui_Bong)
        Ui_Bongsbongs.setObjectName("centralwidget")

        # 여기 값들이 받을 값들이다. 
        self.completed_value = 2
        self.max_value = 10
        self.Folder_name = str(bongja)
        self.MLFB = "A2C154670091"
        
        self.progressBar = QtWidgets.QProgressBar(Ui_Bongsbongs)
        self.progressBar.setGeometry(QtCore.QRect(20, 190, 321, 31))
        self.progressBar.setMaximum(self.max_value)      # 이건 추가해 준건데 받아야 할 BOM의 개수를 max_value로 한것이다.
        self.progressBar.setProperty("value", self.completed_value)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Ui_Bongsbongs)
        self.label.setGeometry(QtCore.QRect(20, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Ui_Bongsbongs)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Ui_Bongsbongs)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Ui_Bongsbongs)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Ui_Bongsbongs)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")

        self.result_label1 = QtWidgets.QLabel(Ui_Bongsbongs)
        self.result_label1.setGeometry(QtCore.QRect(120, 100, 171, 21))
        self.result_label1.setObjectName("result_label1")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_label1.setFont(font)
        self.result_label2 = QtWidgets.QLabel(Ui_Bongsbongs)
        self.result_label2.setGeometry(QtCore.QRect(120, 130, 171, 21))
        self.result_label2.setObjectName("result_label2")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_label2.setFont(font)
        self.result_label3 = QtWidgets.QLabel(Ui_Bongsbongs)
        self.result_label3.setGeometry(QtCore.QRect(90, 160, 171, 21))
        self.result_label3.setObjectName("result_label3")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_label3.setFont(font)
        # Ui_Bong.setCentralWidget(Ui_Bongsbongs)
        # self.statusbar = QtWidgets.QStatusBar(Ui_Bong)
        # self.statusbar.setObjectName("statusbar")
        # Ui_Bong.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_Bong)
        QtCore.QMetaObject.connectSlotsByName(Ui_Bong)  

    def retranslateUi(self, Ui_Bong):
        _translate = QtCore.QCoreApplication.translate
        Ui_Bong.setWindowTitle(_translate("Ui_Bong", "BOM Downloader"))
        self.label.setText(_translate("Ui_Bong", "Current"))
        self.label_2.setText(_translate("Ui_Bong", "Status"))
        self.label_3.setText(_translate("Ui_Bong", " - Folder: "))
        self.label_4.setText(_translate("Ui_Bong", " - MLFB:"))
        self.pushButton.setText(_translate("Ui_Bong", "START (F5 to break)"))
        self.result_label1.setText(_translate("Ui_Bong", self.Folder_name))
        self.result_label2.setText(_translate("Ui_Bong", self.MLFB))
        self.result_label3.setText(_translate("Ui_Bong", "{} out of {}".format(self.completed_value, self.max_value)))

# if __name__ == "__main__":
import sys
app = QtWidgets.QApplication(sys.argv)  # 시작

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#두번째 페이지 돌려주는 loop

for i in range(1,10):
    bongja = i
    time.sleep(5)
    Ui_Bongsbongs = QtWidgets.QWidget()
    ui2 = Ui_Bong()
    ui2.setupUi_2(Ui_Bongsbongs)

sys.exit(app.exec_())   # 끝 -->app이 종료되면 0을 return 해서 python이 무한루프를 빠져나온다. 

