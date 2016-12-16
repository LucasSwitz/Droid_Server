from joysticks.JoystickMonitor import JoystickMonitor
from joysticks.logitechF710.LogitechF710Joystick import LogitechF710Joystick


class HectorOI:
    joystick_base = JoystickMonitor()
    drive_stick = LogitechF710Joystick()
    joystick_base.add_joystick(drive_stick)