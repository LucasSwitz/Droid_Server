from hector.HectorMap import HectorMap
from systems.DriveTrain import DriveTrain
from command.commands.DriveByJoystickCommand import DriveByJoystickCommand


class Hector:

    instance = None
    # Turret Config
    turret_tilt_motor_pins = [HectorMap.TILT_DIRECTION_PIN, HectorMap.TILT_STEP_PIN]
    turret_pan_motor_pins = [HectorMap.PAN_DIRECTION_PIN, HectorMap.PAN_STEP_PIN]
    # turret = Turret(turret_pan_motor_pins, turret_tilt_motor_pins)

    # DriveTrain Config
    drivetrain = DriveTrain.get_instance()
    drivetrain.set_default_command(DriveByJoystickCommand())

    systems = {
        # turret.name(): turret,
        drivetrain.name(): drivetrain
    }

    def disable_all_systems(self):
        for system in self.systems.values():
            system.disable()

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
