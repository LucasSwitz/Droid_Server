import abc
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class RPiMotorController:
    def __init__(self, pins):
        self._pins = pins
        self._setup_pins()

    def _setup_pins(self):
        for pin in self._pins:
            GPIO.setup(pin, GPIO.OUT)

    def get_pins(self):
        return self._pins

    @abc.abstractmethod
    def set(self, position):
        """Set Position of actuator"""
        return
