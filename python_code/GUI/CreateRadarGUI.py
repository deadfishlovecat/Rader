# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateRadar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(435, 527)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 80, 101, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.radar_sn = QtWidgets.QLineEdit(Dialog)
        self.radar_sn.setGeometry(QtCore.QRect(170, 90, 191, 21))
        self.radar_sn.setObjectName("radar_sn")
        self.radar_name = QtWidgets.QLineEdit(Dialog)
        self.radar_name.setGeometry(QtCore.QRect(170, 140, 191, 21))
        self.radar_name.setObjectName("radar_name")
        self.lfm_type = QtWidgets.QComboBox(Dialog)
        self.lfm_type.setGeometry(QtCore.QRect(170, 340, 191, 21))
        self.lfm_type.setObjectName("lfm_type")
        self.lfm_type.addItem("")
        self.lfm_type.addItem("")
        self.pri_type = QtWidgets.QComboBox(Dialog)
        self.pri_type.setGeometry(QtCore.QRect(170, 240, 191, 21))
        self.pri_type.setObjectName("pri_type")
        self.pri_type.addItem("")
        self.pri_type.addItem("")
        self.pri_type.addItem("")
        self.pri_type.addItem("")
        self.fs_type = QtWidgets.QComboBox(Dialog)
        self.fs_type.setGeometry(QtCore.QRect(170, 290, 191, 21))
        self.fs_type.setObjectName("fs_type")
        self.fs_type.addItem("")
        self.fs_type.addItem("")
        self.fs_type.addItem("")
        self.fs_type.addItem("")
        self.single_fs = QtWidgets.QCheckBox(Dialog)
        self.single_fs.setGeometry(QtCore.QRect(170, 190, 91, 19))
        self.single_fs.setObjectName("single_fs")
        self.LFM = QtWidgets.QCheckBox(Dialog)
        self.LFM.setGeometry(QtCore.QRect(270, 190, 91, 19))
        self.LFM.setObjectName("LFM")
        self.sure = QtWidgets.QPushButton(Dialog)
        self.sure.setGeometry(QtCore.QRect(110, 420, 61, 28))
        self.sure.setObjectName("sure")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 420, 61, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "新建雷达："))
        self.label.setText(_translate("Dialog", "雷达编号"))
        self.label_5.setText(_translate("Dialog", "雷达名字"))
        self.label_9.setText(_translate("Dialog", "信号类型"))
        self.label_8.setText(_translate("Dialog", "重频类型"))
        self.label_7.setText(_translate("Dialog", "频率类型"))
        self.label_11.setText(_translate("Dialog", "LFM类型"))
        self.lfm_type.setItemText(0, _translate("Dialog", "大带宽LFM"))
        self.lfm_type.setItemText(1, _translate("Dialog", "频率捷变LFM"))
        self.pri_type.setItemText(0, _translate("Dialog", "重频脉组"))
        self.pri_type.setItemText(1, _translate("Dialog", "重频参差"))
        self.pri_type.setItemText(2, _translate("Dialog", "重频抖动"))
        self.pri_type.setItemText(3, _translate("Dialog", "重频固定"))
        self.fs_type.setItemText(0, _translate("Dialog", "频率固定"))
        self.fs_type.setItemText(1, _translate("Dialog", "频率分集"))
        self.fs_type.setItemText(2, _translate("Dialog", "频率脉间捷变"))
        self.fs_type.setItemText(3, _translate("Dialog", "频率脉组捷变"))
        self.single_fs.setText(_translate("Dialog", "单频信号"))
        self.LFM.setText(_translate("Dialog", "线性调频"))
        self.sure.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))

