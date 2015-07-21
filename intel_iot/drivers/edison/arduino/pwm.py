from intel_iot.drivers.generic.pwm import Pwm
from intel_iot.util import gpio


class Pwm(Pwm):
    def __init__(self, pin_config):
        super().__init__(pin_config)
        gpio.configure_out(pin_config["out_pin"], 1)
        gpio.configure_in(pin_config["pullup_pin"])
