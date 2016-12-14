from systems.Turret import Turret


class Hector:
    turret_tilt_motor_pins = [5, 6]
    turret_pan_motor_pins = [26, 19]
    turret = Turret(turret_pan_motor_pins, turret_tilt_motor_pins)

    systems = {
        turret.name(): turret
    }
