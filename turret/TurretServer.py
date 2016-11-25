from communication.server.Server import Server
from turret.InputChannel import InputChannel, InputMode


class TurretServer(Server):
    def __init__(self, port, input_mode=InputMode.CLI):
        super(TurretServer, self).__init__(port)
        self.inputChannel = InputChannel(input_mode)

    def on_data_recieve(self, data):
        self.inputChannel.parseData(data)

