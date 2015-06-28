from intel_iot.board.edison import board, ADC


class Joystick:
    def __init__(self, pin_x, pin_y):
        self._pin_x = board.setup(pin_x + 14, ADC)
        self._pin_y = board.setup(pin_y + 14, ADC)

    def read_x(self):
        return self._pin_x.value

    def read_y(self):
        return self._pin_y.value