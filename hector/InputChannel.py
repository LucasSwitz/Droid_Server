from command.CLInterpreter import CLInterpreter
from enum import Enum
from binascii import hexlify
from hector.HectorOI import HectorOI


class InputMode(Enum):
    CLI = 0,
    TELEOP = 1


class InputChannel:
    def __init__(self, mode=InputMode.CLI):
        self._mode = mode
        self._joystick_base = HectorOI.joystick_base

    def parseData(self, data):
        switch = {
            InputMode.CLI: self.parse_cli,
            InputMode.TELEOP: self.parse_teleop,
        }

        parser = switch.get(self._mode)

        parser(data)

    def parse_cli(self, data):
        cli = CLInterpreter()
        data = self.normalize_string(data)
        (base_command, args) = self.get_cli_command(data)
        cli.run_cli_command(base_command, args)

    def parse_teleop(self, data):
        new_data = [0] * len(data)
        for i in range(0, len(data)):
            hex_value = hexlify(data[i])
            new_data[i] = int(hex_value, 16)
        self._joystick_base.update_joystick(new_data[0], new_data[1:len(new_data)])

    def get_cli_command(self, user_input):
        base_command = ""
        for c in str(user_input):
            if c == " ":
                return base_command, self.get_cli_args(user_input[len(base_command) + 1:len(user_input)])
            base_command += c
        return base_command, None

    def get_cli_args(self, args_input):
        args = []
        current_arg = ""
        for c in args_input:
            if c == ' ':
                args.append(current_arg)
                current_arg = ""
            else:
                current_arg += c

        args.append(current_arg)
        return args

    def change_mode(self, mode):
        self._mode = mode

    @staticmethod
    def normalize_string(string):
        while '  ' in string:
            string = str.replace(string, '  ', ' ')
        if string[len(string) - 1] == ' ':
            string = string[0:len(string) - 1]
        if string[0] == ' ':
            string = string[1:len(string)]
        return string
