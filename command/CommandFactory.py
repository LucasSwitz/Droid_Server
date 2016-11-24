from command.commands.PanToPositionCommand import PanToPositionCommand


class CommandFactory:
    @staticmethod
    def get_command(command_name, args):
        switch = {
            "pan_to_position": PanToPositionCommand.from_args(args)
        }
        return switch.get(command_name).run()

    def parse_command(self, args):
        command_name = args[0]
        command_args = args[1:]
        return self.get_command(command_name, command_args)