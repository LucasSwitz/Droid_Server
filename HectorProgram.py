from AbstractHectorProgram import AbstractHectorProgram
from hector.Hector import Hector
from command.CommandQueue import CommandQueue


class HectorProgram(AbstractHectorProgram):
    def teleop(self):
        CommandQueue.get_instance().run()

    def on_auto_start(self):
        pass

    def auto(self):
        pass

    def disabled(self):
        pass

    def on_disabled_start(self):
        Hector.stop()

    def on_teleop_start(self):
        CommandQueue.get_instance().clear()
