# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.SNR_Data = QtWidgets.QLineEdit(self.centralwidget)
        self.SNR_Data.setGeometry(QtCore.QRect(140, 50, 61, 21))
        self.SNR_Data.setObjectName("SNR_Data")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.low_ad_fs = QtWidgets.QCheckBox(self.centralwidget)
        self.low_ad_fs.setGeometry(QtCore.QRect(140, 90, 91, 19))
        self.low_ad_fs.setObjectName("low_ad_fs")
        self.mid_ad_fs = QtWidgets.QCheckBox(self.centralwidget)
        self.mid_ad_fs.setGeometry(QtCore.QRect(140, 120, 91, 19))
        self.mid_ad_fs.setObjectName("mid_ad_fs")
        self.high_ad_fs = QtWidgets.QCheckBox(self.centralwidget)
        self.high_ad_fs.setGeometry(QtCore.QRect(140, 150, 101, 19))
        self.high_ad_fs.setObjectName("high_ad_fs")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 40, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 180, 61, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 170, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 210, 91, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pdw_button = QtWidgets.QPushButton(self.centralwidget)
        self.pdw_button.setGeometry(QtCore.QRect(240, 210, 51, 28))
        self.pdw_button.setObjectName("pdw_button")
        self.signal_button = QtWidgets.QPushButton(self.centralwidget)
        self.signal_button.setGeometry(QtCore.QRect(240, 240, 51, 28))
        self.signal_button.setObjectName("signal_button")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 240, 91, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.create_radar = QtWidgets.QPushButton(self.centralwidget)
        self.create_radar.setGeometry(QtCore.QRect(440, 280, 93, 28))
        self.create_radar.setObjectName("create_radar")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 280, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 330, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 320, 901, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(300, 0, 20, 331))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(210, 350, 72, 15))
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 350, 71, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(440, 350, 72, 15))
        self.label_12.setObjectName("label_12")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(510, 350, 71, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(590, 350, 21, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(370, 350, 21, 16))
        self.label_15.setObjectName("label_15")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(80, 380, 741, 161))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 280, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 280, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(360, 50, 481, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "雷达信号分选仿真系统"))
        self.label.setText(_translate("MainWindow", "环境SNR:"))
        self.label_2.setText(_translate("MainWindow", "电磁环境参数设置:"))
        self.label_3.setText(_translate("MainWindow", "AD驻留波段:"))
        self.low_ad_fs.setText(_translate("MainWindow", "0-400M"))
        self.mid_ad_fs.setText(_translate("MainWindow", "400-800M"))
        self.high_ad_fs.setText(_translate("MainWindow", "800-1200M"))
        self.label_4.setText(_translate("MainWindow", "(dB)"))
        self.label_5.setText(_translate("MainWindow", "仿真时间:"))
        self.label_6.setText(_translate("MainWindow", "(ms)"))
        self.label_8.setText(_translate("MainWindow", "PDW输出目录:"))
        self.pdw_button.setText(_translate("MainWindow", "选择"))
        self.signal_button.setText(_translate("MainWindow", "选择"))
        self.label_10.setText(_translate("MainWindow", "信号输出目录:"))
        self.label_7.setText(_translate("MainWindow", "雷达仿真参数设置:"))
        self.create_radar.setText(_translate("MainWindow", "新建雷达"))
        self.pushButton_2.setText(_translate("MainWindow", "清空雷达"))
        self.label_9.setText(_translate("MainWindow", "原始信号观测:"))
        self.label_11.setText(_translate("MainWindow", "起始时间:"))
        self.label_12.setText(_translate("MainWindow", "结束时间:"))
        self.label_14.setText(_translate("MainWindow", "us"))
        self.label_15.setText(_translate("MainWindow", "us"))
        self.pushButton_3.setText(_translate("MainWindow", "修改"))
        self.pushButton_4.setText(_translate("MainWindow", "保存"))

