# A Hate Story
from libintel.util import gpio
from libintel.util.file import read_file


class Analogue:
    def __init__(self, pin_config):
        gpio.configure_out(pin_config["out_pin"])
        gpio.configure_in(pin_config["pullup_pin"])

        self._sysfs_path = "/sys/bus/iio/devices/iio:device1/in_voltage{}_raw".format(
            pin_config["pin_modes"]["analogue"]["channel"])

    @property
    def value(self):
        return int(read_file(self._sysfs_path))