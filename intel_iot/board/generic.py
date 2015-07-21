from intel_iot.util import gpio

# Pin mode constants
GPIO_IN = "gpio_in"
GPIO_OUT = "gpio_out"
ADC = "adc"
PWM = "pwm"

class Board:
    def setup(self, pin, mode):
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
            self.setup(*pair)
        # END FUCK

        gpio_pin = pin_config["gpio_pin"]
        gpio.export(gpio_pin)

        gpio.set_mode(gpio_pin, mode_config.get("pin_mode", 0))

        _apply_mux(self._config.get("post_mux", {}))
        return self._drivers[mode](pin_config)

    def __init__(self, config, drivers):
        self._config = config
        self._drivers = drivers
