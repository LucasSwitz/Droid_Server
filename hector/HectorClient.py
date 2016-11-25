from communication.server.Client import ClientThread
from communication.MessageDispatch import MessageDispatch


class HectorClient(ClientThread, MessageDispatch.DispatchListener):
    def handle(self, message):
        ClientThread.send(self, str.encode(message))
