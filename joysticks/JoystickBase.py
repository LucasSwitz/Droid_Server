from joysticks.Button import Button

class JoystickBase:
    def __init__(self):
        self.joysticks = dict()

    def add_joystick(self, stick):
        print "adding joystick"
        self.joysticks[stick.get_id()] = stick

    def update_joystick(self, joystick_id, button_values):
        if joystick_id in self.joysticks.keys():
            stick = self.joysticks[joystick_id]
            stick.get_button(Button.XL_ID).update(button_values[0])
            stick.get_button(Button.YL_ID).update(button_values[1])
            stick.get_button(Button.XR_ID).update(button_values[2])
            stick.get_button(Button.YR_ID).update(button_values[3])
