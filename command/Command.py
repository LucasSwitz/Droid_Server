import abc


class Command:
    def __init__(self, parallel=False):
        self._parallel = parallel
        self.switches = {
            "-p": Command.set_parallel(self, True)
        }

    def is_parallel(self):
        return self._parallel

    @abc.abstractmethod
    def init(self):
        """Called once at the start of the Command"""

    @abc.abstractmethod
    def finished(self):
        """Returned true when the Command is finished"""

    @abc.abstractmethod
    def execute(self):
        """Called until command is finished"""

    @abc.abstractmethod
    def end(self):
        """Called when command ends"""

    def set_attributes(self, args):
        for arg in args:
            self.switches.get(arg)

    @staticmethod
    def from_args(args):
        """Returns object of Class from parsed string"""
        return Command()

    def set_parallel(self, parallel):
        self._parallel = parallel

    def run(self):
        self.init()
        while not self.finished():
            self.execute()
        self.end()
