import abc
from command.CommandQueue import CommandQueue
from enum import Enum
from hector.Hector import Hector


class HectorMode(Enum):
    DISABLED = 0
    TELEOP = 1
    AUTONOMOUS = 2


class AbstractHectorProgram:
    def __init__(self):
        self._last_mode = None
        self.change_mode(HectorMode.DISABLED)

    def on_teleop_start(self):
        CommandQueue.get_instance().clear()
        Hector.get_instance().enable_all_systems()
        self._on_teleop_start()

    def on_auto_start(self):
        CommandQueue.get_instance().clear()
        Hector.get_instance().enable_all_systems()
        self._on_auto_start()

    def on_disabled_start(self):
        CommandQueue.get_instance().clear()
        Hector.get_instance().disable_all_systems()
        self._on_disabled_start()

    @abc.abstractmethod
    def _on_auto_start(self):
        """called once at the start of auto"""
        return

    @abc.abstractmethod
    def _on_teleop_start(self):
        """called once at the start of teleop"""
        return

    @abc.abstractmethod
    def _on_disabled_start(self):
        """called once at the start of disabled"""
        return

    @abc.abstractmethod
    def auto(self):
        """main auto loop"""
        return

    @abc.abstractmethod
    def teleop(self):
        """main teleop loop"""
        return

    @abc.abstractmethod
    def disabled(self):
        """main disabled loop"""
        return

    def run(self):
        while Hector.get_instance().is_alive():
            if self._mode == HectorMode.DISABLED:
                if self._last_mode != HectorMode.DISABLED:
                    self.on_disabled_start()
                self.disabled()
            elif self._mode == HectorMode.TELEOP:
                if self._last_mode != HectorMode.TELEOP:
                    self.on_teleop_start()
                self.teleop()
            elif self._mode == HectorMode.AUTONOMOUS:
                if self._last_mode != HectorMode.AUTONOMOUS:
                    self.on_auto_start()
                self.auto()
            self._last_mode = self._mode

    def change_mode(self, mode):
        self._mode = mode

    def get_mode(self):
        return self._mode

    def start_command_queue(self):
        CommandQueue.get_instance().run()

    def stop_command_queue(self):
        CommandQueue.get_instance().clear()
