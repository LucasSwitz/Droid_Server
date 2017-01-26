from bot.BotServer import BotServer
from hector.Hector import Hector

server = BotServer(4444, Hector.get_instance())
server.start()
