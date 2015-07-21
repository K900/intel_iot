# A Hate Story
from intel_iot.util import gpio
from intel_iot.util.file import read_file


class Adc:
    def __init__(self, pin_config):
        gpio.configure_out(pin_config["out_pin"])
        gpio.configure_in(pin_config["pullup_pin"])

        self._sysfs_path = "/sys/bus/iio/devices/iio:device1/in_voltage{}_raw".format(
            pin_config["pin_modes"]["analogue"]["channel"])

    @property
    def value(self):
        return int(read_file(self._sysfs_path))