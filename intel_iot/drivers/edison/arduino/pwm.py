from intel_iot.drivers.generic.pwm import Pwm
from intel_iot.util import gpio


class EdisonArduinoPwm(Pwm):
    """
    PWM output driver for the Intel Edison Arduino board, based on the generic PWM driver.
    This simply adds some GPIO twiddling logic/sanity checks before constructing the wrapper.
    """

    def __init__(self, pin_config):
        gpio.configure_out(pin_config["out_pin"], 1)
        gpio.configure_in(pin_config["pullup_pin"])
        super().__init__(pin_config)
