from joysticks.Joystick import Joystick
from Button import Button


class LogitechF710Joystick(Joystick):
    LOGITECH_F710_PRODUCT_ID = 0xc21f

    def __init__(self):
        Joystick.__init__(self, 0)
        self.add_button(Button(Button.XL_ID))
        self.add_button(Button(Button.YL_ID))
        self.add_button(Button(Button.XR_ID))
        self.add_button(Button(Button.YR_ID))

    def get_leftY(self):
        return (self.get_button(Button.YL_ID).get_value()-128)/128.0

    def get_rightY(self):
        return (self.get_button(Button.YR_ID).get_value()-128)/128.0
