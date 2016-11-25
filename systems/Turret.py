from systems.System import System
from motorcontrollers.RPiStepperMotorController import RPiSetepperMotorController


class Turret(System):
    def __init__(self):
        super(Turret,self).__init__("Turret")
        self._pan_controller = RPiSetepperMotorController()
        self._tilt_controller = RPiSetepperMotorController()

    def set_pan(self, angle):
        self._pan_controller.set(angle)

    def set_tilt(self, angle):
        self._tilt_controller.set(angle)

    def tilt_angle(self):
        return self._tilt_controller.get_current_position()

    def pan_angle(self):
        return self._pan_controller.get_current_position()
