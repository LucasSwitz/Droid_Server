from command.commands.StepTurretByDPad import StepTurretByDPad
from systems.Turret import Turret
from systems.DriveTrain import DriveTrain
from systems.Laser import Laser
from command.commands.DriveByJoystickCommand import DriveByJoystickCommand
from command.commands.LaserStateByButtonCommand import LaserStateByButtonCommand

class Hector:
    instance = None
    # Turret Config
    turret = Turret.get_instance()
    turret.set_default_command(StepTurretByDPad())

    # DriveTrain Config
    drivetrain = DriveTrain.get_instance()
    drivetrain.set_default_command(DriveByJoystickCommand())

    laser = Laser.get_instance()
    laser.set_default_command(LaserStateByButtonCommand())

    systems = {
        turret.name(): turret,
        drivetrain.name(): drivetrain,
        laser.name(): laser
    }

    def disable_all_systems(self):
        for system in self.systems.values():
            system.stop()

    def enable_all_systems(self):
        for system in self.systems.values():
            system.enable()

    @staticmethod
    def get_instance():
        if Hector.instance is None:
            Hector.instance = Hector()
        return Hector.instance

    def is_alive(self):
        return self._alive

    def kill(self):
        self._alive = False

    def __init__(self):
        self._alive = True
