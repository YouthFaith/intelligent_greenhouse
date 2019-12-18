# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(635, 535)
        mainwindow.setMinimumSize(QtCore.QSize(635, 535))
        mainwindow.setMaximumSize(QtCore.QSize(635, 535))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/png/ui_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainwindow.setWindowIcon(icon)
        mainwindow.setStyleSheet("color: rgb(86, 118, 162);")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(mainwindow)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(mainwindow)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ui_refresh = QtWidgets.QPushButton(mainwindow)
        self.ui_refresh.setMinimumSize(QtCore.QSize(50, 0))
        self.ui_refresh.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.ui_refresh.setFont(font)
        self.ui_refresh.setObjectName("ui_refresh")
        self.horizontalLayout.addWidget(self.ui_refresh)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ui_scrollArea = QtWidgets.QScrollArea(mainwindow)
        self.ui_scrollArea.setWidgetResizable(True)
        self.ui_scrollArea.setObjectName("ui_scrollArea")
        self.ui_scroll_area = QtWidgets.QWidget()
        self.ui_scroll_area.setGeometry(QtCore.QRect(0, 0, 613, 473))
        self.ui_scroll_area.setObjectName("ui_scroll_area")
        self.ui_layout = QtWidgets.QGridLayout(self.ui_scroll_area)
        self.ui_layout.setContentsMargins(2, 2, 2, 2)
        self.ui_layout.setSpacing(2)
        self.ui_layout.setObjectName("ui_layout")
        self.ui_scrollArea.setWidget(self.ui_scroll_area)
        self.verticalLayout.addWidget(self.ui_scrollArea)
        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "智能大棚---主界面"))
        self.label.setText(_translate("mainwindow", "监控台"))
        self.ui_refresh.setText(_translate("mainwindow", "更新"))

