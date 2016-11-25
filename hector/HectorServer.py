from communication.server.Server import Server
from hector.InputChannel import InputChannel, InputMode
from hector.HectorClient import HectorClient
from communication.MessageDispatch import MessageDispatch


class HectorServer(Server):
    def __init__(self, port, input_mode=InputMode.CLI):
        Server.__init__(self, port)
        self.inputChannel = InputChannel(input_mode)
        self.message_dispatch = MessageDispatch()

    def on_data_recieve(self, data):
        self.inputChannel.parseData(data)

    def add_client(self, client_socket):
        client = HectorClient(client_socket)
        client.add_recieve_listener(self)
        self.message_dispatch.add_listener(client)
        client.start()
