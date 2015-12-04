from intel_iot.util.file import read_file


class IioVoltage:
    """
    Generic IIO voltage driver. May be useful for many kinds of IIO devices, but only tested with ADCs.
    """

    def __init__(self, device_id, channel):
        self._sysfs_path = "/sys/bus/iio/devices/iio:device{}/in_voltage{}_raw".format(device_id, channel)

    @property
    def value(self):
        """
        The raw value from the IIO device.
        :return: Raw IIO device reading.
        """
        return int(read_file(self._sysfs_path))
