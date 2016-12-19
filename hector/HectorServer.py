from communication.MessageDispatch import MessageDispatch
from communication.server.Server import Server
from hector.AbstractHectorProgram import HectorMode
from hector.Hector import Hector
from hector.HectorClient import HectorClient
from hector.HectorPacket import HectorPacket
from hector.HectorProgram import HectorProgram
from hector.input.CLIInputState import CLIInputState
from hector.input.TeleopInputState import TeleopInputState
from hector.input.InputChannel import InputChannel
from binascii import hexlify

class HectorServer(Server):
    def __init__(self, port):
        Server.__init__(self, port)
        MessageDispatch()
        self.inputChannel = InputChannel()
        self._hector_program = HectorProgram()
        self._hector_program.change_mode(HectorMode.TELEOP)

    def start(self):
        Server.start(self)
        while not self.has_client():
            pass
        self._hector_program.run()

    def add_client(self, client_socket):
        client = HectorClient(client_socket)
        client.add_recieve_listener(self)
        MessageDispatch.instance.add_listener(client)
        client.start()

    def on_data_recieve(self, data):
        if data == "close":
            MessageDispatch.instance.dispatch("Server Closing....")
            Hector.get_instance().disable_all_systems()
            Server.stop(self)

        data = self.to_hex(data)
        self.parse_hector_packet(data)

    @staticmethod
    def to_hex(data):
        new_data = [0]*len(data)
        for i in range(0,len(data)):
            new_data[i] = hexlify(data[i])

        return new_data

    def parse_hector_packet(self, data):
        self._check_input_state(data[HectorPacket.INPUT_MODE_BYTE])
        self._check_hector_mode(data[HectorPacket.HECTOR_MODE_BYTE])
        self.inputChannel.parseData(data[HectorPacket.JOYSTICK_RESERVE_START:len(data)])

    def _check_input_state(self, state):
        input_mode = None
        if int(state,16) == HectorPacket.CLI_INPUT_MODE:
            input_mode = CLIInputState()
        elif int(state,16) == HectorPacket.TELEOP_INPUT_MODE:
            input_mode = TeleopInputState()

        if self.inputChannel.get_input_state().__class__ != input_mode.__class__:
            self.inputChannel.change_input_state(input_mode)

    def _check_hector_mode(self, mode):

        modes = {
            HectorPacket.HECTOR_MODE_DISABLED: HectorMode.DISABLED,
            HectorPacket.HECTOR_MODE_AUTO: HectorMode.AUTONOMOUS,
            HectorPacket.HECTOR_MODE_TELEOP: HectorMode.TELEOP
        }

        hector_mode = modes.get(mode)

        if self._hector_program.get_mode() != hector_mode:
            self._hector_program.change_mode(hector_mode)
