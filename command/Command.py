import abc


class Command:

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
    @abc.abstractstaticmethod
    def from_args(args):
        """Returns object of Class from parsed string"""
        return Command()

    def run(self):
        self.init()
        while not self.finished():
            self.execute()
        self.end()
