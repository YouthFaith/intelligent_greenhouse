# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_verify.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_show_face(object):
    def setupUi(self, show_face):
        show_face.setObjectName("show_face")
        show_face.resize(642, 572)
        show_face.setStyleSheet("background-image: url(:/1.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(show_face)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(show_face)
        self.label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(86, 118, 162);")
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.video_label = QtWidgets.QLabel(show_face)
        self.video_label.setMinimumSize(QtCore.QSize(600, 450))
        self.video_label.setAutoFillBackground(False)
        self.video_label.setStyleSheet("")
        self.video_label.setText("")
        self.video_label.setScaledContents(True)
        self.video_label.setObjectName("video_label")
        self.verticalLayout.addWidget(self.video_label)
        self.ui_prompt = QtWidgets.QLabel(show_face)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(18)
        self.ui_prompt.setFont(font)
        self.ui_prompt.setText("")
        self.ui_prompt.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_prompt.setObjectName("ui_prompt")
        self.verticalLayout.addWidget(self.ui_prompt)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(show_face)
        QtCore.QMetaObject.connectSlotsByName(show_face)

    def retranslateUi(self, show_face):
        _translate = QtCore.QCoreApplication.translate
        show_face.setWindowTitle(_translate("show_face", "Form"))
        self.label_2.setText(_translate("show_face", "人脸验证"))

