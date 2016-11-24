from command.Command import Command


class PanToPositionCommand(Command):
    def __init__(self, degree):
        super(PanToPositionCommand, self).__init__()
        self._degree = degree

    def execute(self):
        pass

    def init(self):
        print("Panning to degree: "+str(self._degree))

    def end(self):
        pass

    def from_args(args):
        return PanToPositionCommand(int(args[0]))

    def finished(self):
        pass
