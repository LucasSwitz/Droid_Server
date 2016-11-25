import abc
from command.CommandQueue import CommandQueue


class AbstractTurretProgram:
    def __init__(self):
        super(AbstractTurretProgram, self).__init__()
        self._commandQueue = CommandQueue()

    @abc.abstractmethod
    def on_stop(self):
        """What to do when the turret is stopped"""
        return

    @abc.abstractmethod
    def on_start(self):
        """ What to do when the turrent turns on"""
        return
