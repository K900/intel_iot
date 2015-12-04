from intel_iot.drivers.generic.gpio import GpioIn
from intel_iot.util import gpio


class EdisonArduinoGpioIn(GpioIn):
    """
    Intel Edison Arduino board GPIO input driver. Provides pullup resistor control in addition to basic functionality.
    """
    def __init__(self, value, direction, pullup):
        super().__init__(value)
        self._direction = direction
        self._pullup = pullup

    @property
    def pullup(self):
        """
        The current state of the pullup resistors for this GPIO.
        :return: True if the input is pulled up, False otherwise.
        """
        return gpio.get_direction(self._pullup) == gpio.DIRECTION_OUT and gpio.get(self._pullup)

    @pullup.setter
    def pullup(self, value):
        if value:
            gpio.configure_out(self._pullup, 1)
        else:
            gpio.configure_in(self._pullup)
