from communication.server.Server import Server
from hector.InputChannel import InputChannel, InputMode
from hector.HectorClient import HectorClient
from hector.Hector import Hector
from communication.MessageDispatch import MessageDispatch
from hector.HectorProgram import HectorProgram
from hector.AbstractHectorProgram import HectorMode


class HectorServer(Server):
    def __init__(self, port, input_mode=InputMode.CLI):
        Server.__init__(self, port)
        MessageDispatch()
        self.inputChannel = InputChannel(input_mode)
        self._hector_program = HectorProgram()
        self._hector_program.change_mode(HectorMode.TELEOP)

    def start(self):
        Server.start(self)
        while not self.has_client():
            pass
        self._hector_program.run()

    def on_data_recieve(self, data):
        if data == "close":
            MessageDispatch.instance.dispatch("Server Closing....")
            Server.stop(self)
            Hector.get_instance().disable_all_systems()
        self.inputChannel.parseData(data)

    def add_client(self, client_socket):
        client = HectorClient(client_socket)
        client.add_recieve_listener(self)
        MessageDispatch.instance.add_listener(client)
        client.start()

    def change_input_mode(self, mode):
        self.inputChannel.change_mode(mode)
