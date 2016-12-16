from RPiMotorController import RPiMotorController
import RPi.GPIO as GPIO


class PWMMotorController(RPiMotorController):
    def __init__(self, pins):
        RPiMotorController.__init__(self, pins)

    def set(self, value):
        if value == 0:
            self.off()
        elif value < 0:
            self.apply_backwards(value)
        else:
            self.apply_forward(value)

    def apply_forward(self, throttle):
        print("Forward!")
        GPIO.output(self.get_pins()[0], True)
        GPIO.output(self.get_pins()[1], False)

    def apply_backwards(self, throttle):
        print("Backward!")
        GPIO.output(self.get_pins()[1], True)
        GPIO.output(self.get_pins()[0], False)

    def off(self):
        print ("Off!")
        GPIO.output(self.get_pins()[1], False)
        GPIO.output(self.get_pins()[0], False)