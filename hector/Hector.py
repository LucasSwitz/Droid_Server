from systems.Turret import Turret


class Hector:
    turret_pan_motor_pins = [1, 2, 3, 4]
    turret_tilt_motor_pins = [1, 2, 3, 4]

    turret = Turret(turret_pan_motor_pins, turret_tilt_motor_pins)
