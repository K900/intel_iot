from libintel.util import gpio
from libintel.util.file import write_file


def apply_mux(conf):
    for pin, value in conf.items():
        gpio.configure_out(pin, value)


class Board:
    def configure(self, pin, mode):
        apply_mux(self._config.get("pre_mux", {}))

        pin_config = self._config["pins"][pin]
        mode_config = pin_config["pin_modes"][mode]

        apply_mux(mode_config.get("mux", {}))

        # FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK
        depends = mode_config.get("depends", {})
        for pin, mode in depends.items():
            self.configure(pin, mode)
        # END FUCK

        gpio_pin = pin_config["gpio_pin"]
        gpio.export(gpio_pin)

        write_file("/sys/kernel/debug/gpio_debug/gpio{}/current_pinmux".format(gpio_pin),
                   "mode{}".format(mode_config.get("pin_mode", 0)))

        apply_mux(self._config.get("post_mux", {}))
        return mode_config["class"](pin_config)

    def __init__(self, config):
        self._config = config
