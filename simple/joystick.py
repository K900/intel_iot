from intel_iot.board.edison import board


class Joystick:
    def __init__(self, pin_x, pin_y):
        self._pin_x = board.configure(pin_x + 14, "analogue")
        self._pin_y = board.configure(pin_y + 14, "analogue")

    def read_x(self):
        return self._pin_x.value

    def read_y(self):
        return self._pin_y.value