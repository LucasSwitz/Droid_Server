from System import System
from motorcontrollers.PWMMotorController import PWMMotorController
from functools import partial
from hector.HectorOI import HectorOI
from threading import Thread
from command.commands.DriveByJoystickCommand import DriveByJoystickCommand


class DriveTrain(System):
    def get_default_command(self, args):
        return DriveByJoystickCommand()

    def __init__(self, left_pins, right_pins):
        System.__init__(self, "DriveTrain")
        self._left_motor_controller = PWMMotorController(left_pins)
        self._right_motor_controller = PWMMotorController(right_pins)
        self._stick = HectorOI.drive_stick

    def enable(self):
        thread = Thread(target=self.run())
        thread.daemon = True
        thread.start()

    def set(self, left_throttle, right_throttle):
        if abs(right_throttle) < .5:
            right_throttle = 0
        if abs(left_throttle) < .5:
            left_throttle = 0
        System.dispatch_message(self, "Driving...")
        self._left_motor_controller.set(left_throttle)
        self._right_motor_controller.set(right_throttle)

    def run(self):
        self.set(HectorOI.drive_stick.get_left_Y(), HectorOI.drive_stick.get_right_Y())

    def stop(self):
        System.dispatch_message(self, "Stopped!")
        self._left_motor_controller.set(0)
        self._right_motor_controller.set(0)

    def get_cli_functions(self, args):
        functions = {
            "stop": partial(self.stop)
        }
        if len(args) > 1:
            functions["drive"] = partial(self.set, int(args[0]), int(args[1]))

        return functions
