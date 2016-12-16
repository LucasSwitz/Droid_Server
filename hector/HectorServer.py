from communication.server.Server import Server
from hector.InputChannel import InputChannel, InputMode
from hector.HectorClient import HectorClient
from hector.Hector import Hector
from communication.MessageDispatch import MessageDispatch
import sys


class HectorServer(Server):
    def __init__(self, port, input_mode=InputMode.CLI):
        MessageDispatch()
        Server.__init__(self, port)
        self.inputChannel = InputChannel(input_mode)
        #Hector.drivetrain.enable()

    def on_data_recieve(self, data):
        if data == "close":
            MessageDispatch.instance.dispatch("Server Closing....")
            Server.stop(self)
            sys.exit()
        self.inputChannel.parseData(data)

    def add_client(self, client_socket):
        client = HectorClient(client_socket)
        client.add_recieve_listener(self)
        MessageDispatch.instance.add_listener(client)
        client.start()
