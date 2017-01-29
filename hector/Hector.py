from bot.Bot import Bot
from hector.commands.DriveByJoystickCommand import DriveByJoystickCommand
from hector.commands.LaserStateByButtonCommand import LaserStateByButtonCommand
from hector.commands.StepTurretByDPad import StepTurretByDPad
from hector.systems.DriveTrain import DriveTrain
from hector.systems.Laser import Laser
from hector.systems.Turret import Turret


class Hector(Bot):
    instance = None

    # DriveTrain Config
    drivetrain = DriveTrain.get_instance()
    drivetrain.set_default_command(DriveByJoystickCommand())

    @staticmethod
    def get_instance():
        if Hector.instance is None:
            Hector.instance = Hector()
        return Hector.instance

    def __init__(self):
        Bot.__init__(self)
