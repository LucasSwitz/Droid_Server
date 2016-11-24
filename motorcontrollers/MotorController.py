import abc


class MotorController:
    def __init__(self, port):
        self._port = port

    def get_port(self):
        return self._port

    @abc.abstractmethod
    def set(self,position):
        """Set Position of actuator"""
        return