from hector.input.InputState import InputState
from binascii import hexlify
from joysticks.JoystickMonitor import JoystickMonitor


class TeleopInputState(InputState):
    def parse(self, data):
        new_data = [0] * len(data)
        for i in range(0, len(data)):
            hex_value = hexlify(data[i])
            new_data[i] = int(hex_value, 16)
        JoystickMonitor.get_instance().update_joystick(new_data[0], new_data[1:len(new_data)])