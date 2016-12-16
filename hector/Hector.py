from systems.Turret import Turret
from systems.DriveTrain import DriveTrain
from HectorMap import HectorMap



class Hector:
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

