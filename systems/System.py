from communication.MessageDispatch import MessageDispatch


class System:

    def __init__(self, name):
        self._locked = False
        self._name = name

    def lock(self):
        self._locked = True

    def name(self):
        return self._name

    def __str__(self):
        return self.name()

    def dispatch_message(self, message):
        MessageDispatch.instance.dispatch(str(self) + ": " + message)
