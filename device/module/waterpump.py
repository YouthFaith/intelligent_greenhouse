import RPi.GPIO as GPIO


class WaterPump:
    water_pump_pin = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            WaterPump.water_pump_pin = args[0]
            GPIO.setup(WaterPump.water_pump_pin, GPIO.OUT)
            GPIO.output(WaterPump.water_pump_pin, GPIO.LOW)
            WaterPump.safe_init()
        return cls.instance

    def __init__(self, pin):
        pass

    @staticmethod
    def safe_init():
        GPIO.output(WaterPump.water_pump_pin, GPIO.LOW)

    @staticmethod
    def start_pump():
        GPIO.output(WaterPump.water_pump_pin, GPIO.HIGH)

    @staticmethod
    def stop_pump():
        GPIO.output(WaterPump.water_pump_pin, GPIO.LOW)
