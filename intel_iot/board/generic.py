from intel_iot.drivers.adc import Adc
from intel_iot.drivers.gpio import GpioIn, GpioOut
from intel_iot.drivers.pwm import Pwm
from intel_iot.util import gpio
from intel_iot.util.file import write_file

# Pin mode constants
GPIO_IN = "gpio_in"
GPIO_OUT = "gpio_out"
ADC = "adc"
PWM = "pwm"

DRIVERS = {
    GPIO_IN: GpioIn,
    GPIO_OUT: GpioOut,
    ADC: Adc,
    PWM: Pwm
}

class Board:
    def configure(self, pin, mode):
        def _apply_mux(conf):
            for pair in conf.items():
                gpio.configure_out(*pair)

        _apply_mux(self._config.get("pre_mux", {}))

        pin_config = self._config["pins"][pin]

        pin_modes = pin_config["pin_modes"]
        if mode not in pin_modes:
            raise ValueError(
                'Unsupported pin mode {} for pin {}! Supported modes: {}'.format(mode, pin, ', '.join(pin_modes)))

        try:
            mode_config = pin_config["pin_modes"][mode]
        except (KeyError, TypeError):
            mode_config = {}

        _apply_mux(mode_config.get("mux", {}))

        # FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK
        depends = mode_config.get("depends", {})
        for pair in depends.items():
            self.configure(*pair)
        # END FUCK

        gpio_pin = pin_config["gpio_pin"]
        gpio.export(gpio_pin)

        write_file("/sys/kernel/debug/gpio_debug/gpio{}/current_pinmux".format(gpio_pin),
                   "mode{}".format(mode_config.get("pin_mode", 0)))

        _apply_mux(self._config.get("post_mux", {}))
        return DRIVERS[mode](pin_config)

    def __init__(self, config):
        self._config = config
