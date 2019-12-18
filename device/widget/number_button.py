# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal
class MyPushButton(QPushButton):
    num_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicked.connect(self.emit_str)

    def emit_str(self):
        num = self.text()
        self.num_signal.emit(num)