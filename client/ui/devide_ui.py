# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devide.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_device(object):
    def setupUi(self, device):
        device.setObjectName("device")
        device.resize(880, 518)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        device.setFont(font)
        device.setStyleSheet("color: rgb(86, 118, 162);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(device)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.video_monitor = QtWidgets.QLabel(device)
        self.video_monitor.setMinimumSize(QtCore.QSize(500, 500))
        self.video_monitor.setMaximumSize(QtCore.QSize(500, 500))
        self.video_monitor.setText("")
        self.video_monitor.setObjectName("video_monitor")
        self.horizontalLayout.addWidget(self.video_monitor)
        self.frame = QtWidgets.QFrame(device)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.name = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.horizontalLayout_5.addWidget(self.name)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.current_temp = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        self.current_temp.setFont(font)
        self.current_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.current_temp.setObjectName("current_temp")
        self.horizontalLayout_6.addWidget(self.current_temp)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.current_hum = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        self.current_hum.setFont(font)
        self.current_hum.setAlignment(QtCore.Qt.AlignCenter)
        self.current_hum.setObjectName("current_hum")
        self.horizontalLayout_7.addWidget(self.current_hum)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.information = QtWidgets.QTextBrowser(self.frame)
        self.information.setObjectName("information")
        self.verticalLayout.addWidget(self.information)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(device)
        QtCore.QMetaObject.connectSlotsByName(device)

    def retranslateUi(self, device):
        _translate = QtCore.QCoreApplication.translate
        device.setWindowTitle(_translate("device", "监控台---详细信息"))
        self.label_3.setText(_translate("device", "农作物"))
        self.name.setText(_translate("device", "玫瑰"))
        self.label_4.setText(_translate("device", "当前湿度"))
        self.current_temp.setText(_translate("device", "25"))
        self.label_5.setText(_translate("device", "当前温度"))
        self.current_hum.setText(_translate("device", "12"))
        self.information.setHtml(_translate("device", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

