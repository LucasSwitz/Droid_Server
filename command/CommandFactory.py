from command.commands.PanToPositionCommand import PanToPositionCommand
from communication.MessageDispatch import MessageDispatch


class CommandFactory:
    @staticmethod
    def get_command(command_name, args):
        switch = {
            "pan_to_position": PanToPositionCommand.from_args(args)
        }
        (command, args) = switch.get(command_name)

        if command is None:
            MessageDispatch.instance.dispatch("Invalid command: " + command_name)
        else:
            command.set_attributes(args)

        return command

    def parse_command(self, args):
        if args is None or len(args) < 1:
            MessageDispatch.instance.dispatch("Invalid use of 'execute' ")
            return
        command_name = args[0]
        command_args = args[1:]
        return self.get_command(command_name, command_args)
