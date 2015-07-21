from intel_iot.drivers.generic.gpio import GpioBase, GpioIn, GpioOut
from intel_iot.util import gpio


class _EdisonArduinoGpioBase(GpioBase):
    def __init__(self, pin_config):
        super().__init__(pin_config)
        self._out_pin = pin_config["out_pin"]
        self._pullup_pin = pin_config["pullup_pin"]


# noinspection PyAbstractClass
class EdisonArduinoGpioIn(GpioIn, _EdisonArduinoGpioBase):
    """
    Intel Edison Arduino board GPIO input driver.
    Provides automated muxing.
    """
    def __init__(self, pin_config):
        super().__init__(pin_config)
        gpio.configure_out(self._out_pin)
        gpio.configure_in(self._pullup_pin)

    @property
    def pullup(self):
        """
        Get the current state of the pullup resistors for this GPIO.
        :return: True if the input is pulled up, False otherwise.
        """
        return gpio.get_direction(self._pullup_pin) == gpio.DIRECTION_OUT and gpio.get(self._pullup_pin)

    @pullup.setter
    def pullup(self, value):
        """
        Set the state of the pullup resistors for this GPIO.
        :param value: True if the input should be pulled up, False otherwise.
        :return: None
        """
        if value:
            gpio.configure_out(self._pullup_pin, 1)
        else:
            gpio.configure_in(self._pullup_pin)


class EdisonArduinoGpioOut(GpioOut, _EdisonArduinoGpioBase):
    """
    Intel Edison Arduino board GPIO output driver.
    Provides automated muxing.
    """
    def __init__(self, pin_config):
        super().__init__(pin_config)
        gpio.configure_out(self._out_pin, 1)
        gpio.configure_in(self._pullup_pin)
