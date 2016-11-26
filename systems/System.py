from communication.MessageDispatch import MessageDispatch
import abc


class System:
    def __init__(self, name):
        self._locked = False
        self._name = name

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

    def lock(self):
        self._locked = True

    def name(self):
        return self._name

    def __str__(self):
        return self.name()

    def dispatch_message(self, message):
        MessageDispatch.instance.dispatch(str(self) + ": " + message)
