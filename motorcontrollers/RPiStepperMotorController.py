from motorcontrollers.MotorController import MotorController
import RPI.GPIO as GPIO


class RPiSetepperMotorController(MotorController):
    sequence = \
        [[1, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [1, 0, 0, 1]]

    def __init__(self, port, pins, steps=200):
        super(RPiSetepperMotorController, self).__init__(port)
        self._pins = pins
        self._current_position = 0
        self._goal_position = 0
        self.setup_pins()
        self.MAX_STEPS = steps

    def setup_pins(self):
        for pin in self._pins:
            GPIO.setup(pin, GPIO.OUT)

    def set(self, position):
        self.step_to_angle(position)

    def step_to_angle(self, angle):
        self.step_to_position(self.convert_angle_to_step(angle))

    def step_to_position(self, position):

        if position > self.MAX_STEPS:
            position = self.MAX_STEPS

        self._goal_position = position

        while self._current_position != position:
            for pin in range(0, 4):
                xpin = self._pins[pin]
                if self.sequence[self._current_position % len(self.sequence)][pin] != 0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            self._current_position += 1

            if self._current_position >= self.MAX_STEPS:
                self._current_position = self.MAX_STEPS

    def on_target(self):
        return self._goal_position == self._current_position

    def get_current_step(self):
        return self._current_position

    def get_current_angle(self):
        return self.convert_step_to_angle(self._current_position)

    @staticmethod
    def convert_angle_to_step(angle):
        return angle * (5 / 9)

    @staticmethod
    def convert_step_to_angle(step):
        return step * (9 / 5)
