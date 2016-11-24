from communication.server.Server import Server
from enum import Enum
from command.CLInterpreter import CLInterpreter


class ServerMode(Enum):
    CLI = 0,
    TELEOP = 1


class TurretServer(Server):
    def __init__(self, port, mode=ServerMode.CLI):
        super(TurretServer, self).__init__(port)
        self.mode = mode

    def on_data_recieve(self, data):
        self.parseData(data)

    def parse_cli(self, data):
        cli = CLInterpreter()
        (base_command,args) = self.get_cli_command(data)
        cli.run_cli_command(base_command, args)

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

    def parse_teleop(self, data):
        return

    def parseData(self, data):

        switch = {
            ServerMode.CLI: self.parse_cli,
            ServerMode.TELEOP: self.parse_teleop,
        }

        parser = switch.get(self.mode)

        parser(data)

    def change_mode(self, mode):
        self.mode = mode
