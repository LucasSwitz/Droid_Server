from communication.MessageDispatch import MessageDispatch
from command.CommandQueue import CommandQueue
import abc


class System:
    def __init__(self, name):
        self._locked = False
        self._name = name
        self._default_command = self.get_default_command()
        self._current_command = False

    def cli_input(self, args):
        function = self.get_cli_functions(args[1:len(args)]).get(args[0])

        if function is None:
            System.dispatch_message(self, "Invalid function requested")
            return

        function()

    @abc.abstractmethod
    def get_cli_functions(self, args):
        """Return CLI functions"""
        return

    @abc.abstractmethod
    def stop(self):
        """stops all electrical components"""
        return

    @abc.abstractmethod
    def get_default_command(self, args):
        """Returns default command. None if no command"""
        return

    def lock(self, command):
        if self._current_command is not None:
            if self._current_command.is_interruptable():
                self._current_command.interrupt()
            else:
                return False

        self._current_command = command
        self._locked = True
        return True

    def is_locked(self):
        return self._locked

    def release(self):
        self._locked = False
        if self._default_command is not None:
            self.set_current_command(self._default_command)
            self.run_default_command()

    def set_default_command(self, command):
        self._default_command = command

    def set_current_command(self,command):
        self._current_command = command

    def run_default_command(self):
        CommandQueue.get_instance().add_command(self._default_command)

    def name(self):
        return self._name

    def __str__(self):
        return self.name()

    def dispatch_message(self, message):
        MessageDispatch.instance.dispatch(str(self) + ": " + message)
