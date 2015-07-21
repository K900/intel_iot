import os.path
from intel_iot.board.generic import PWM

from intel_iot.util.file import write_ignore_busy, read_file, write_file


class Pwm:
    """
    Generic PWM signal driver for Linux /sys/class/pwm interfaces.
    """

    def __init__(self, pin_config):
        conf = pin_config["pin_modes"][PWM]
        pwm_id = conf["pwm_id"]
        pwmchip_id = conf.get("pwmchip_id", 0)

        self._sysfs_root = "/sys/class/pwm/pwmchip{}/pwm{}/".format(pwmchip_id, pwm_id)
        write_ignore_busy("/sys/class/pwm/pwmchip{}/export".format(pwmchip_id), str(pwm_id))

    def _option_path(self, option):
        return os.path.join(self._sysfs_root, option)

    def _write_int(self, option, value):
        return write_file(self._option_path(option), str(value))

    def _read_int(self, option):
        return int(read_file(self._option_path(option)))

    @property
    def enabled(self):
        """
        Checks whether the PWM output is enabled.
        :return: True if the output is currently enabled; False otherwise.
        """
        return bool(read_file(self._option_path('enable')))

    @enabled.setter
    def enabled(self, value):
        """
        Enables or disables the PWM output.
        :param value: True if the output is to be enabled, False otherwise.
        :return: None
        """
        if value:
            write_file(self._option_path('enable'), '1')
        else:
            write_file(self._option_path('enable'), '0')

    @property
    def duty_cycle(self):
        """
        Reads the duty cycle (active time) value of the PWM signal in nanoseconds.
        :return: The duty cycle of the PWM signal.
        """
        return self._read_int('duty_cycle')

    @duty_cycle.setter
    def duty_cycle(self, value):
        """
        Sets the duty cycle (active time) value of the PWM signal in nanoseconds.
        :param value: The new duty cycle value.
        :return: None
        """
        self._write_int('duty_cycle', value)

    @property
    def period(self):
        """
        Reads the period (total time) value of the PWM signal in nanoseconds.
        :return: The period of the PWM signal.
        """
        return self._read_int('period')

    @period.setter
    def period(self, value):
        """
        Sets the period value of the PWM signal in nanoseconds.
        :param value: The new period value.
        :return: None
        """
        self._write_int('period', value)
