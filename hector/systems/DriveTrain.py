from functools import partial

from hector.HectorMap import HectorMap

from System import System
from hector.HectorOI import HectorOI
from motorcontrollers.PWMMotorController import PWMMotorController


class DriveTrain(System):
    instance = None

    @staticmethod
    def get_instance():
        if DriveTrain.instance is None:
            DriveTrain.instance = DriveTrain([HectorMap.DRIVETRAIN_LEFT_FWD, HectorMap.DRIVETRAIN_LEFT_BKWD]
                                             , [HectorMap.DRIVETRAIN_RIGHT_FWD, HectorMap.DRIVETRAIN_RIGHT_BKWD])
        return DriveTrain.instance

    def __init__(self, left_pins, right_pins):
        System.__init__(self, "DriveTrain")
        self._left_motor_controller = PWMMotorController(left_pins)
        self._right_motor_controller = PWMMotorController(right_pins)
        self._stick = HectorOI.drive_stick

    def _enable(self):
        pass

    def set(self, left_throttle, right_throttle):
        if abs(right_throttle) < .5:
            right_throttle = 0
        if abs(left_throttle) < .5:
            left_throttle = 0
        self._left_motor_controller.set(left_throttle)
        self._right_motor_controller.set(right_throttle)

    def stop(self):
        self._left_motor_controller.set(0)
        self._right_motor_controller.set(0)

    def get_cli_functions(self, args):
        functions = {
            "stop": partial(self.stop)
        }
        if len(args) > 1:
            functions["drive"] = partial(self.set, int(args[0]), int(args[1]))

        return functions
