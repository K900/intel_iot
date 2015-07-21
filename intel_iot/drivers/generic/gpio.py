from intel_iot.util import gpio


class _GpioBase:
    def __init__(self, pin_config):
        self._gpio_pin = pin_config["gpio_pin"]

    @property
    def value(self):
        return gpio.get(self._gpio_pin)

class GpioIn(_GpioBase):
    def __init__(self, pin_config):
        super().__init__(pin_config)
        gpio.configure_in(self._gpio_pin)

    # noinspection PyMethodOverriding
    @_GpioBase.value.setter
    def value(self, value):
        raise NotImplementedError("Cannot write to read only GPIO!")

class GpioOut(_GpioBase):
    def __init__(self, pin_config):
        super().__init__(pin_config)
        self._gpio_pin = pin_config["gpio_pin"]
        gpio.configure_out(self._gpio_pin)

    @_GpioBase.value.setter
    def value(self, value):
        gpio.set(self._gpio_pin, value)
