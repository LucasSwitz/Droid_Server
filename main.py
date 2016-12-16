from hector.HectorServer import HectorServer
from hector.InputChannel import InputMode

server = HectorServer(4444, input_mode=InputMode.TELEOP)
server.start()
