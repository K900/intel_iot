import os.path

from intel_iot.util.file import write_ignore_busy, read_file, write_file


class Pwm:
    """
    Generic PWM signal driver for Linux /sys/class/pwm interfaces.
    """

    def __init__(self, chip_id, pwm_id):
        self._sysfs_root = "/sys/class/pwm/pwmchip{}/pwm{}/".format(chip_id, pwm_id)
        write_ignore_busy("/sys/class/pwm/pwmchip{}/export".format(chip_id), str(pwm_id))

        self.enabled = False
        self.duty_cycle = 0

    def _option_path(self, option):
        return os.path.join(self._sysfs_root, option)

    def _write_int(self, option, value):
        return write_file(self._option_path(option), str(value))

    def _read_int(self, option):
        return int(read_file(self._option_path(option)))

    @property
    def enabled(self):
        """
        Whether the PWM is enabled, i.e. actively outputting a signal.
        :return: True if the output is currently enabled; False otherwise.
        """
        return bool(read_file(self._option_path('enable')))

    @enabled.setter
    def enabled(self, value):
        if value:
            write_file(self._option_path('enable'), '1')
        else:
            write_file(self._option_path('enable'), '0')

    @property
    def duty_cycle(self):
        """
        The duty cycle (active time) value of the PWM signal in nanoseconds.
        :return: The duty cycle of the PWM signal.
        """
        return self._read_int('duty_cycle')

    @duty_cycle.setter
    def duty_cycle(self, value):
        self._write_int('duty_cycle', value)

    @property
    def period(self):
        """
        The period (total time) value of the PWM signal in nanoseconds.
        :return: The period of the PWM signal.
        """
        return self._read_int('period')

    @period.setter
    def period(self, value):
        self._write_int('period', value)
