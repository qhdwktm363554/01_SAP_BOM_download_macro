# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '210713_BOM_importer_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from sys import hexversion
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import bong
from bong import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.FramelessWindowHint
        MainWindow.resize(347, 241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 여기 값들이 받을 값들이다. 
        self.completed_value = 2
        self.max_value = 10
        # self.Folder_name = "my thing"
        self.MLFB = "A2C154670091"
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 190, 321, 31))
        self.progressBar.setMaximum(self.max_value)      # 이건 추가해 준건데 받아야 할 BOM의 개수를 max_value로 한것이다.
        self.progressBar.setProperty("value", self.completed_value)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")

        self.result_label1 = QtWidgets.QLabel(self.centralwidget)
        self.result_label1.setGeometry(QtCore.QRect(120, 100, 171, 21))
        self.result_label1.setObjectName("result_label1")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_label1.setFont(font)
        self.result_label2 = QtWidgets.QLabel(self.centralwidget)
        self.result_label2.setGeometry(QtCore.QRect(120, 130, 171, 21))
        self.result_label2.setObjectName("result_label2")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_label2.setFont(font)
        self.result_label3 = QtWidgets.QLabel(self.centralwidget)
        self.result_label3.setGeometry(QtCore.QRect(90, 160, 171, 21))
        self.result_label3.setObjectName("result_label3")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_label3.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BOM Downloader"))
        self.label.setText(_translate("MainWindow", "Current"))
        self.label_2.setText(_translate("MainWindow", "Status"))
        self.label_3.setText(_translate("MainWindow", " - Folder: "))
        self.label_4.setText(_translate("MainWindow", " - MLFB:"))
        self.pushButton.setText(_translate("MainWindow", "START (F5 to break)"))
        self.result_label1.setText(_translate("MainWindow", Folder_name))
        self.result_label2.setText(_translate("MainWindow", self.MLFB))
        self.result_label3.setText(_translate("MainWindow", "{} out of {}".format(self.completed_value, self.max_value)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

