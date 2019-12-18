# -*- coding: utf-8 -*-
# from PyQt5.QtNetwork import QUdpSocket
from PyQt5.QtWidgets import QApplication
import sys
from mainwindow import MainWindow
from module.monitor import Monitor
from module.aliyun_api import ALApi
from module.light import Light
from module.waterpump import WaterPump
from module.airconditioner import AirConditioner
from module.door import Door
from module.alert import Alert
from module.thsensor import ThSensor
import RPi.GPIO as GPIO
LEFT_DOOR_PIN = 20
RIGHT_DOOR_PIN = 21
AIR_CONDITIONER_PIN = 17
WATER_PUMP_PIN = 5
RED_LIGHT_PIN = 19
GREEN_LIGHT_PIN = 26
TEMP_HUM_PIN = 13
ALERT_PIN = 16


def init_system():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    set_low()
    ALApi()
    Monitor()
    Alert(ALERT_PIN)
    Light(RED_LIGHT_PIN, GREEN_LIGHT_PIN)
    WaterPump(WATER_PUMP_PIN)
    AirConditioner(AIR_CONDITIONER_PIN)
    Door(LEFT_DOOR_PIN, RIGHT_DOOR_PIN)
    th = ThSensor(TEMP_HUM_PIN)
    th.start()

def set_low():
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_system()
    main = MainWindow()
    sys.exit(app.exec_())
