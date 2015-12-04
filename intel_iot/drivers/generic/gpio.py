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
        Get the current value of the GPIO.
        :return: The current value of the GPIO.
        """
        return gpio.get(self._gpio)


class GpioIn(GpioBase):
    """
    Generic GPIO input driver. Provides sanity checking.
    """

    def __init__(self, gpio_no):
        super().__init__(gpio_no)
        gpio.configure_in(self._gpio)

    # noinspection PyMethodOverriding
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
    @GpioBase.value.setter
    def value(self, value):
        """
        Sets the current value of the GPIO.
        :param value: The value to set.
        :return:
        """
        gpio.set(self._gpio, value)
