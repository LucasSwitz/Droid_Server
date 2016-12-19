from systems.Turret import Turret
from command.Command import Command
from hector.HectorOI import HectorOI
import time

class StepTurretByJoystickCommand(Command):
    def init(self):
        pass

    def execute(self):
        x_throttle = self._stick.get_left_X()
        print "X Throttle: "+str(x_throttle)
        if abs(x_throttle) > .5:
            if x_throttle > 0:
                Turret.get_instance().step_pan(True)
            else:
                Turret.get_instance().step_pan(False)

    def finished(self):
        return False

    def end(self):
        pass

    def _interrupted(self):
        self.end()

    def __init__(self):
        Command.__init__(self)
        self.uses(Turret.get_instance())
        self._stick = HectorOI.drive_stick
