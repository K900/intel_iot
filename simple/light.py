from intel_iot.board.edison import board


class Light:
    def __init__(self, pin):
        self._pin = board.configure(pin + 14, "analogue")

    def read(self):
        return self._pin.value