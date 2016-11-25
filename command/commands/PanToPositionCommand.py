from command.Command import Command
from hector.Hector import Hector


class PanToPositionCommand(Command):
    def __init__(self, degree):
        Command.__init__(self)
        self._degree = degree

    def execute(self):
        pass

    def init(self):
        Hector.turret.set_pan(self._degree)

    def end(self):
        pass

    @staticmethod
    def from_args(args):
        if len(args) < 1:
            return None
        command = PanToPositionCommand(int(args[0]))

        return command, args[1:len(args)]

    def finished(self):
        return Hector.turret.is_at_pan_target() and Hector.turret.is_at_tilt_target()
