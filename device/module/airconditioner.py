# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO


class AirConditioner:
    air_conditioner_pin = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            AirConditioner.air_conditioner_pin = args[0]
            GPIO.setup(AirConditioner.air_conditioner_pin, GPIO.OUT)
            GPIO.output(AirConditioner.air_conditioner_pin, GPIO.LOW)
            AirConditioner.safe_init()
        return cls.instance

    def __init__(self, pin):
        pass

    @staticmethod
    def safe_init():
        GPIO.output(AirConditioner.air_conditioner_pin, GPIO.LOW)

    @staticmethod
    def turn_on_air():
        GPIO.output(AirConditioner.air_conditioner_pin, GPIO.HIGH)

    @staticmethod
    def turn_off_air():
        GPIO.output(AirConditioner.air_conditioner_pin, GPIO.LOW)
