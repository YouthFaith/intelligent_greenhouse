import RPi.GPIO as GPIO


class Light:
    red_light_pin = 0
    green_light_pin = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            Light.red_light_pin = args[0]
            Light.green_light_pin = args[1]
            GPIO.setup(Light.red_light_pin, GPIO.OUT)
            GPIO.setup(Light.green_light_pin, GPIO.OUT)
            GPIO.output(Light.red_light_pin, GPIO.LOW)
            GPIO.output(Light.green_light_pin, GPIO.LOW)
            Light.safe_init()
        return cls.instance

    def __init__(self, red_pin, green_pin):
        pass

    @staticmethod
    def safe_init():
        GPIO.output(Light.red_light_pin, GPIO.LOW)
        GPIO.output(Light.green_light_pin, GPIO.LOW)

    @staticmethod
    def turn_on_red_light():
        GPIO.output(Light.red_light_pin, GPIO.HIGH)

    @staticmethod
    def turn_on_green_light():
        GPIO.output(Light.green_light_pin, GPIO.HIGH)

    @staticmethod
    def turn_off_red_light():
        GPIO.output(Light.red_light_pin, GPIO.LOW)

    @staticmethod
    def turn_off_green_light():
        GPIO.output(Light.green_light_pin, GPIO.LOW)

if __name__ == "__main__":
    Light(19, 26)
    Light.turn_on_green_light()
