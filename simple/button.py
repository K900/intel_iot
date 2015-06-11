import noise


class Button(noise.Noise):
    def __init__(self, pin):
        super().__init__(pin)
        self._conf.pullup = 1
