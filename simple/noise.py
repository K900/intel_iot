import blink


class Noise(blink.Pin):
    def __init__(self, pin):
        super().__init__(pin, "in")

    # noinspection PyMethodMayBeStatic
    def read(self):
        return 1 - super().read()
