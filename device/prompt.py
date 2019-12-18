# -*- coding: utf-8 -*-
from ui.prompt_ui import Ui_Dialog
from PyQt5.QtWidgets import QDialog
class Prompt(QDialog, Ui_Dialog):
    def __init__(self, label, parent=None):
        super(Prompt, self).__init__(parent)
        self.setupUi(self)
        self.label.setText(label)

    def showEvent(self, a0):
        self.startTimer(1000)

    def timerEvent(self, a0):
        self.accept()