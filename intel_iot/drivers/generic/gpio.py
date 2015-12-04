from intel_iot.util import gpio


class GpioBase:
    """
    Generic GPIO (digital I/O) base class. Don't create instances of this directly, use GpioIn/GpioOut instead.
    """

    def __init__(self, gpio_no):
        self._gpio = gpio_no

    @property
    def value(self):
        """
        The current value of the GPIO.
        :return: The current value of the GPIO.
        """
        return gpio.get(self._gpio)


class GpioIn(GpioBase):
    """
    Generic GPIO input driver. Provides additional sanity checking by preventing writes.
    """

    def __init__(self, gpio_no):
        super().__init__(gpio_no)
        gpio.configure_in(self._gpio)

    # noinspection PyMethodOverriding
    # PyCharm goes crazy when properties are involved. This is actually correct.
    @GpioBase.value.setter
    def value(self, value):
        raise NotImplementedError("Cannot write to read only GPIO!")


class GpioOut(GpioBase):
    """
    Generic GPIO output driver.
    """

    def __init__(self, gpio_no):
        super().__init__(gpio_no)
        gpio.configure_out(self._gpio)

    # noinspection PyMethodOverriding
    # PyCharm goes crazy when properties are involved. This is actually correct.
    @GpioBase.value.setter
    def value(self, value):
        gpio.set(self._gpio, value)
