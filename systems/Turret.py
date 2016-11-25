from systems.System import System
from motorcontrollers.RPiStepperMotorController import RPiSetepperMotorController


class Turret(System):
    def __init__(self, pan_pins, tilt_pins):
        System.__init__(self, "Turret")
        self._pan_controller = RPiSetepperMotorController(0, pan_pins)
        self._tilt_controller = RPiSetepperMotorController(0, tilt_pins)

    def set_pan(self, angle):
        System.dispatch_message(self, "Panning to " + str(angle) + " degrees...")
        self._pan_controller.set(angle)

    def set_tilt(self, angle):
        pass
        self._tilt_controller.set(angle)

    def tilt_angle(self):
        pass
        return self._tilt_controller.get_current_angle()

    def pan_angle(self):
        pass
        return self._pan_controller.get_current_angle()

    def is_at_pan_target(self):
        pass
        return self._pan_controller.on_target()

    def is_at_tilt_target(self):
        pass
        return self._tilt_controller.on_target()
