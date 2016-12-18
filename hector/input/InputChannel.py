class InputChannel:
    def __init__(self, state):
        self._state = state

    def parseData(self, data):
        self._state.parse(data)

    def change_input_state(self, state):
        self._state = state

    def get_input_state(self):
        return self._state
