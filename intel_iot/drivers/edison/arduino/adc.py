# A Hate Story
from intel_iot.board.generic import ADC
from intel_iot.util import gpio
from intel_iot.util.file import read_file


class EdisonArduinoAdc:
    """
    Intel Edison Arduino board ADC driver. May be useful for other IIO devices, too.
    """

    def __init__(self, pin_config):
        gpio.configure_out(pin_config["out_pin"])
        gpio.configure_in(pin_config["pullup_pin"])

        self._sysfs_path = "/sys/bus/iio/devices/iio:device1/in_voltage{}_raw".format(
            pin_config["pin_modes"][ADC]["channel"])

    @property
    def value(self):
        """
        Reads the raw value from the ADC.
        :return: Raw ADC reading (0-4096).
        """
        return int(read_file(self._sysfs_path))
