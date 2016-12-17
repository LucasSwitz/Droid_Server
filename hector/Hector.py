from hector.HectorMap import HectorMap
from systems.DriveTrain import DriveTrain


class Hector:

    instance = None
    # Turret Config
    turret_tilt_motor_pins = [HectorMap.TILT_DIRECTION_PIN, HectorMap.TILT_STEP_PIN]
    turret_pan_motor_pins = [HectorMap.PAN_DIRECTION_PIN, HectorMap.PAN_STEP_PIN]
    # turret = Turret(turret_pan_motor_pins, turret_tilt_motor_pins)

    # DriveTrain Config
    drivetrain_left_motor_pins = [HectorMap.DRIVETRAIN_LEFT_FWD, HectorMap.DRIVETRAIN_LEFT_BKWD]
    drivetrain_right_motor_pins = [HectorMap.DRIVETRAIN_RIGHT_FWD, HectorMap.DRIVETRAIN_RIGHT_BKWD]
    drivetrain = DriveTrain(drivetrain_left_motor_pins, drivetrain_right_motor_pins)

    systems = {
        # turret.name(): turret,
        drivetrain.name(): drivetrain
    }

    def disable_all_systems(self):
        for system in self.systems:
            system.disable()

    def enable_all_systems(self):
        for system in self.systems:
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
