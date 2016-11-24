from motorcontrollers.MotorController import MotorController


class RaspberryPiMotorController(MotorController):
    def __init__(self, port):
        super(RaspberryPiMotorController,self,port).__init__()

    def set(self,position):
        print("going to position")