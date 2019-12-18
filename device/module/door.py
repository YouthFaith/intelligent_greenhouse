# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
from module.light import Light

class Door:
    left_door = 0
    right_door = 0
    left_door_pwm = 0
    right_door_pwm = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            Door.left_door = args[0]
            Door.right_door = args[1]
            GPIO.setup(Door.left_door, GPIO.OUT)
            GPIO.setup(Door.right_door, GPIO.OUT)
            GPIO.output(Door.left_door, GPIO.LOW)
            GPIO.output(Door.right_door, GPIO.LOW)
            Door.left_door_pwm = GPIO.PWM(Door.left_door, 50)
            Door.right_door_pwm = GPIO.PWM(Door.right_door, 50)
            Door.safe_init()
        return cls.instance

    def __init__(self, left_pin, right_pin):
        pass

    @staticmethod
    def safe_init():
        Door.left_door_pwm.start(0)
        Door.right_door_pwm.start(0)
        time.sleep(1)

    @staticmethod
    def turn_on_door():
        Light.turn_on_green_light()
        Door.left_door_pwm.ChangeDutyCycle(2.5 + 180 / 18)
        Door.right_door_pwm.ChangeDutyCycle(2.5 + 180 / 18)
        time.sleep(1)

    @staticmethod
    def turn_off_door():
        Light.turn_off_green_light()
        Door.left_door_pwm.ChangeDutyCycle(2.5 + 0 / 18)
        Door.right_door_pwm.ChangeDutyCycle(2.5 + 0 / 18)
        time.sleep(1)
