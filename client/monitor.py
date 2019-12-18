# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from device import Device
import zlib

class Monitor(QFrame):
    def __init__(self, ip, parent=None):
        super().__init__(parent)
        self.ip = ip
        self.socket_ = QUdpSocket()
        self.detail_device = None
        self.verticalLayout = QVBoxLayout()
        self.label = QLabel(parent)
        self.label.setMinimumSize(QSize(300, 200))
        self.label.setMaximumSize(QSize(300, 200))
        self.label.setScaledContents(True)
        self.verticalLayout.addWidget(self.label)
        self.monitor = QPushButton(parent)
        self.monitor.setMinimumSize(QSize(300, 20))
        self.monitor.setMaximumSize(QSize(300, 20))
        self.verticalLayout.addWidget(self.monitor)
        self.hide_item()
        self.set_connect()

    def hide_item(self):
        self.monitor.hide()

    def show_item(self, mac, port):
        self.monitor.setText(mac)
        self.monitor.show()
        self.label.show()
        self.socket_.bind(QHostAddress(self.ip), port)
        self.socket_.readyRead.connect(self.show_video)
        self.detail_device = Device(monitor=self)

    def show_video(self):
        data = self.socket_.readDatagram(65535)[0]
        data = zlib.decompress(data)
        video_show = QPixmap()
        video_show.loadFromData(data)
        self.label.setPixmap(video_show)
        self.detail_device.video_monitor.setPixmap(video_show)

    def get_current_image(self):
        return self.label.pixmap()

    def set_connect(self):
        self.monitor.clicked.connect(self.show_detail)

    def show_detail(self):
        self.detail_device.show()
