from joysticks.LogitechF710Joystick import LogitechF710Joystick
from joysticks.JoystickBase import JoystickBase


class HectorOI:
    joystick_base = JoystickBase()
    drive_stick = LogitechF710Joystick()
    joystick_base.add_joystick(drive_stick)