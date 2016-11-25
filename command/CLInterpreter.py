from command.CommandFactory import CommandFactory
from communication.MessageDispatch import MessageDispatch

class CLInterpreter:

    @staticmethod
    def run_execute_command(args):
        factory = CommandFactory()
        command = factory.parse_command(args)

        if command is not None:
            command.run()

    def run_cli_command(self, base, args):
        switch = {
            "execute": self.run_execute_command,
        }

        func = switch.get(base, None)
        if func is not None:
            func(args)
        else:
            MessageDispatch.instance.dispatch("Invalid CLI command")
