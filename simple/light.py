from intel_iot.board.edison import board, ADC


class Light:
    def __init__(self, pin):
        self._pin = board.setup(pin + 14, ADC)

    def read(self):
        return self._pin.value