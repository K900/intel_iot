from intel_iot.util import gpio

# Pin mode constants
GPIO_IN = "gpio_in"
GPIO_OUT = "gpio_out"
ADC = "adc"
PWM = "pwm"
I2C = "i2c"


def _apply_mux(conf):
    for pair in conf.items():
        gpio.configure_out(*pair)


def _get_mode_config(conf, mode):
    pin_modes = conf["pin_modes"]
    if mode not in pin_modes:
        raise ValueError('Unsupported pin mode {}! Supported modes: {}'.format(mode, ', '.join(pin_modes)))

    try:
        return pin_modes[mode]
    except (KeyError, TypeError):
        return {}


def _get_pin_config(conf, pin):
    return conf["pins"][pin]


class Board:
    """
    Generic class for interfacing with a development board.
    """

    def setup(self, pin, mode):
        """
        Sets up a pin header for a specified interaction mode, then returns an object providing an API for it.
        :param pin: Pin number/ID on the development board.
        :param mode: I/O configuration to use, e.g. GPIO input, PWM output, etc.
        :return: Wrapper ('driver') object for the specified configuration.
        """
        _apply_mux(self._config.get("pre_mux", {}))

        pin_config = _get_pin_config(self._config, pin)
        mode_config = _get_mode_config(pin_config, mode)

        _apply_mux(mode_config.get("mux", {}))

        # FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK
        resolutions = {}

        def resolve(res_pin, res_mode):
            pin_config = _get_pin_config(self._config, res_pin)
            mode_config = _get_mode_config(pin_config, res_mode)
            depends = mode_config.get("depends", {})
            for key, value in depends.items():
                if key in resolutions and value != resolutions[key]:
                    raise ValueError("Dependency conflicts, check your configuration!")
                resolutions[key] = value
                resolve(key, value)

        resolve(pin, mode)

        for key, value in resolutions.items():
            self.setup(key, value)
        # END FUCK

        gpio_pin = pin_config["gpio_pin"]
        gpio.export(gpio_pin)
        gpio.set_mode(gpio_pin, mode_config.get("pin_mode", 0))

        _apply_mux(self._config.get("post_mux", {}))
        return self._config["drivers"][mode](pin_config)

    def __init__(self, config):
        """
        Creates a new Board instance based on the configuration object supplied by the caller.
        This shouldn't be used directly unless you are writing a board configuration module.
        Board configuration modules should export an instance of this class as a module level variable.
        :param config: The configuration object describing the board.
        :return: The finished Board object.
        """
        self._config = config
