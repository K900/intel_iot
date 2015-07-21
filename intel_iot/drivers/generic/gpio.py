from intel_iot.util import gpio


class _GpioBase:
    """
    Generic GPIO (digital I/O) base class. Don't create instances of this directly, use GpioIn/GpioOut instead.
    """
    def __init__(self, pin_config):
        self._gpio_pin = pin_config["gpio_pin"]

    @property
    def value(self):
        """
        Get the current value of the GPIO.
        :return: The current value of the GPIO.
        """
        return gpio.get(self._gpio_pin)

class GpioIn(_GpioBase):
    """
    Generic GPIO input driver. Provides sanity checking.
    """
    def __init__(self, pin_config):
        super().__init__(pin_config)
        gpio.configure_in(self._gpio_pin)

    # noinspection PyMethodOverriding
    @_GpioBase.value.setter
    def value(self, value):
        raise NotImplementedError("Cannot write to read only GPIO!")

class GpioOut(_GpioBase):
    """
    Generic GPIO output driver.
    """
    def __init__(self, pin_config):
        super().__init__(pin_config)
        self._gpio_pin = pin_config["gpio_pin"]
        gpio.configure_out(self._gpio_pin)

    @_GpioBase.value.setter
    def value(self, value):
        """
        Sets the current value of the GPIO.
        :param value: The value to set.
        :return:
        """
        gpio.set(self._gpio_pin, value)
