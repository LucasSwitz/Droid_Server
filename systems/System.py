

class System:

    def __init__(self, name):
        self._locked = False
        self._name = name

    def lock(self):
        self._locked = True

    def name(self):
        return self._name