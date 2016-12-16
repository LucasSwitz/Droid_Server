from RPiMotorController import RPiMotorController
from enum import Enum
import RPi.GPIO as GPIO
import time


class H4988StepperMotorController(RPiMotorController):
    # pins[0] = directon pins pin[1] = step pin

    class Direction(Enum):
        FORWARD = 0
        BACKWARD = 1

    def __init__(self, pins):
        RPiMotorController.__init__(self, pins)
        self._current_position = 0
        self._goal_position = 0
        self.set_direction(self.Direction.FORWARD)

    def set(self, value):
        self._goal_position += value
        i = 0
        while i < value:
            self.step_forward()
            i += 1

    def step_forward(self):
        if self._current_direction != self.Direction.FORWARD:
            self.set_direction(self.Direction.FORWARD)

        self.step()

    def step_backward(self):
        if self._current_direction != self.Direction.BACKWARD:
            self.set_direction(self.Direction.BACKWARD)

        self.step()

    def set_direction(self, direction):
        if direction == self.Direction.FORWARD:
            self.set_direction_pin(True)
        elif direction == self.Direction.BACKWARD:
            self.set_direction_pin(False)

    def set_direction_pin(self, state):
        if state:
            self._current_direction = self.Direction.FORWARD
            GPIO.output(self._pins[0], GPIO.HIGH)
        else:
            self._current_direction = self.Direction.BACKWARD
            GPIO.output(self._pins[0], GPIO.LOW)
        #should be 50 microseconds
        time.sleep(.0001)

    def step(self):
        GPIO.output(self._pins[1], GPIO.HIGH)
        #should be 100 microseconds
        time.sleep(.0001)
        GPIO.output(self._pins[1], GPIO.LOW)
        #should be 100 microseconds
        time.sleep(.0001)
        self._current_position += 1
