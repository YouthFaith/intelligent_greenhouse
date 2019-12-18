# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

class Alert:
    alert_pin = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            Alert.alert_pin = args[0]
            GPIO.setup(Alert.alert_pin, GPIO.OUT)
            GPIO.output(Alert.alert_pin, GPIO.LOW)
            Alert.safe_init()
        return cls.instance

    def __init__(self, pin):
        pass

    @staticmethod
    def safe_init():
        GPIO.output(Alert.alert_pin, GPIO.LOW)

    @staticmethod
    def turn_on_alert():
        GPIO.output(Alert.alert_pin, GPIO.HIGH)

    @staticmethod
    def turn_off_alert():
        GPIO.output(Alert.alert_pin, GPIO.LOW)
