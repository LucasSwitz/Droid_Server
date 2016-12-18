from joysticks.Joystick import Joystick
from joysticks.logitechF710.LogitechF710AxisButton import LogitechF710AxisButton
from joysticks.buttons.Button import Button


class LogitechF710Joystick(Joystick):
    LOGITECH_F710_PRODUCT_ID = 0xc21f

    def __init__(self):
        Joystick.__init__(self, 0)
        self.add_button(LogitechF710AxisButton(Button.XL_ID))
        self.add_button(LogitechF710AxisButton(Button.YL_ID))
        self.add_button(LogitechF710AxisButton(Button.XR_ID))
        self.add_button(LogitechF710AxisButton(Button.YR_ID))

    def get_left_Y(self):
        return self.get_button(Button.YL_ID).get_magnitude()

    def get_right_Y(self):
        if self.get_button(Button.YR_ID).get_magnitude() is None:
            print "NO BUTTON"
        return self.get_button(Button.YR_ID).get_magnitude()
