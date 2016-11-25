from AbstractTurretProgram import AbstractTurretProgram


class TurretProgram(AbstractTurretProgram):

    def on_stop(self):
        self._commandQueue.stop()


    def on_start(self):
        self._commandQueue.run()
