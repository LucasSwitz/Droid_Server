from command.Command import Command
from hector.Hector import Hector
from hector.HectorOI import HectorOI


class DriveByJoystickCommand(Command):
    def __init__(self):
        Command.__init__(self, parallel=True)
        self._drive_train = Hector.get_instance().drivetrain
        self._stick = HectorOI.drive_stick
        self.uses(self._drive_train)

    def init(self):
        self._drive_train.displatch_message("Driving with joysticks...")

    def execute(self):
        left_throttle = self._stick.get_left_Y()
        right_throttle = self._stick.get_right_Y()
        self._drive_train.set(left_throttle, right_throttle)

    def _interrupted(self):
        self.end()

    def finished(self):
        return False

    def end(self):
        pass
