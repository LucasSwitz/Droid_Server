from command.CommandFactory import CommandFactory


class CLInterpreter:

    @staticmethod
    def run_execute_command(args):
        factory = CommandFactory()
        command = factory.parse_command(args)
        command.run()

    def run_cli_command(self, base, args):
        switch = {
            "execute": self.run_execute_command,
        }

        func = switch.get(base)
        func(args)
