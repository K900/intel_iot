from intel_iot.util.file import read_file


class IioVoltage:
    """
    Generic IIO voltage (ADC) driver.
    """

    def __init__(self, device_id, channel):
        self._sysfs_path = "/sys/bus/iio/devices/iio:device{}/in_voltage{}_raw".format(device_id, channel)

    @property
    def value(self):
        """
        Voltage value from the IIO device.
        :return: Raw IIO device reading.
        """
        return int(read_file(self._sysfs_path))
