import socket
import abc
from communication.server.Client import ClientThread
from communication.server.ClientListener import ClientListener


class Server(ClientListener):

    @abc.abstractmethod
    def on_data_recieve(self, data):
        """Do something with client data"""
        return

    MAX_NUM_OF_CONNECTIONS = 5

    def __init__(self, port):
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._running = False
        self.setup()

    def setup(self):
        print("Setting up server or port: "+str(self._port))
        self._socket.bind(('localhost', self._port))
        self._socket.listen(Server.MAX_NUM_OF_CONNECTIONS)

    def start(self):
        print("Waiting for clients to connect...")
        self._running = True
        while self._running:
            (clientSocket, address) = self._socket.accept()

            print("Client accepted from: "+str(address))

            client = ClientThread(clientSocket)
            client.add_recieve_listener(self)
            client.start()

    def stop(self):
        self._running = False
