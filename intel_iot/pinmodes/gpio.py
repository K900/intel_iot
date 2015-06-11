from libintel.util import gpio


class _GpioBase:
    def __init__(self, pin_config):
        self._gpio_pin = pin_config["gpio_pin"]
        self._out_pin = pin_config["out_pin"]
        self._pullup_pin = pin_config["pullup_pin"]

    @property
    def value(self):
        return gpio.get(self._gpio_pin)


class GpioIn(_GpioBase):
    def __init__(self, pin_config):
        super().__init__(pin_config)
        gpio.configure_out(self._out_pin)
        gpio.configure_in(self._pullup_pin)
        gpio.configure_in(self._gpio_pin)

    @property
    def pullup(self):
        return gpio.get_direction(self._pullup_pin) == gpio.DIRECTION_OUT and gpio.get(self._pullup_pin)

    @pullup.setter
    def pullup(self, value):
        if value:
            gpio.configure_out(self._pullup_pin, 1)
        else:
            gpio.configure_in(self._pullup_pin)

    # noinspection PyMethodOverriding
    @_GpioBase.value.setter
    def value(self, value):
        raise NotImplementedError("Cannot write to read only GPIO!")


class GpioOut(_GpioBase):
    def __init__(self, pin_config):
        super().__init__(pin_config)
        gpio.configure_out(self._out_pin, 1)
        gpio.configure_in(self._pullup_pin)
        gpio.configure_out(self._gpio_pin)

    # noinspection PyMethodOverriding
    @_GpioBase.value.setter
    def value(self, value):
        gpio.set(self._gpio_pin, value)
