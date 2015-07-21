from intel_iot.drivers.gpio import GpioIn, GpioOut
from intel_iot.util import gpio


class EdisonArduinoGpioIn(GpioIn):
    def __init__(self, pin_config):
        super().__init__(pin_config)
        gpio.configure_out(pin_config["out_pin"])

        self._pullup_pin = pin_config["pullup_pin"]
        gpio.configure_in(self._pullup_pin)

    @property
    def pullup(self):
        return gpio.get_direction(self._pullup_pin) == gpio.DIRECTION_OUT and gpio.get(self._pullup_pin)

    @pullup.setter
    def pullup(self, value):
        if value:
            gpio.configure_out(self._pullup_pin, 1)
        else:
            gpio.configure_in(self._pullup_pin)


class EdisonArduinoGpioOut(GpioOut):
    def __init__(self, pin_config):
        super().__init__(pin_config)
        gpio.configure_out(pin_config["out_pin"], 1)
        gpio.configure_in(pin_config["pullup_pin"])