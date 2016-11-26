from systems.System import System
from functools import partial
import threading

from motorcontrollers.RPiStepperMotorController import RPiSetepperMotorController


class Turret(System):
    def get_cli_functions(self, args):
        functions = {
            "disable": self.disable
        }

        if len(args) > 0:
            functions["set_pan"] = partial(self.set_pan, int(args[0]))
            functions["set_tilt"] = partial(self.set_tilt, int(args[0]))

        if len(args) > 1:
            functions["set_pan_tilt"] = partial(self.set_pan_tilt_parallel, int(args[0]), int(args[1]))

        return functions

    def __init__(self, pan_pins, tilt_pins):
        System.__init__(self, "Turret")
        self._pan_controller = RPiSetepperMotorController(0, pan_pins)
        self._tilt_controller = RPiSetepperMotorController(0, tilt_pins)

    def disable(self):
        System.dispatch_message(self, "Disabled.")
        self._pan_controller.disable()
        self._tilt_controller.disable()

    def set_pan(self, steps):
        System.dispatch_message(self, "Panning to " + str(steps) + " steps...")
        self._pan_controller.take_steps(steps)

    def set_tilt(self, steps):
        System.dispatch_message(self, "Tilting to " + str(steps) + " steps...")
        self._tilt_controller.take_steps(steps)

    def set_pan_tilt_parallel(self, pan_angle, tilt_angle):

        pan_thread = threading.Thread(target=self.set_pan, args=(pan_angle,))
        tilt_thread = threading.Thread(target=self.set_tilt, args=(tilt_angle,))

        pan_thread.start()
        tilt_thread.start()

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
