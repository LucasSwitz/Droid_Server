from AbstractHectorProgram import AbstractHectorProgram
from hector.Hector import Hector
from command.CommandQueue import CommandQueue


class HectorProgram(AbstractHectorProgram):

    def teleop(self):
        CommandQueue.get_instance().run()

    def auto(self):
        pass

    def disabled(self):
        pass

    def _on_auto_start(self):
        pass

    def _on_disabled_start(self):
        pass

    def _on_teleop_start(self):
        pass

