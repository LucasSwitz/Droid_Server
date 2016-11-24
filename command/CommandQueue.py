import queue
from threading import Thread


class CommandQueue:
    def __init__(self):
        self._q = queue.Queue()

    def add_command(self, command):
        self._q.put(command)

    def run(self):
        while self._q.not_empty():
            command = self._q.get()
            if command.is_parallel():
                thread = Thread(command.run())
                thread.daemon = True
                thread.start()
            else:
                command.run()
