from intel_iot.board.edison import board


class Pin:
    def __init__(self, pin, direction="in"):
        self._pin = pin
        self._direction = direction
        self._conf = None
        self._reconfigure()

    def _reconfigure(self):
        self._conf = board.configure(self._pin, "gpio_" + self._direction)

    def mode(self, mode):
        assert mode in ('in', 'out')
        self._direction = mode
        self._reconfigure()

    def write(self, value):
        assert value in (0, 1)
        self._conf.value = value

    def read(self):
        return self._conf.value