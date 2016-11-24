import queue


class CommandQueue:
    def __init__(self):
        self._q = queue.Queue()

    def add_command(self, command):
        self._q.put(command)

    def run(self):
        while self._q.not_empty():
            self._q.get().run()
