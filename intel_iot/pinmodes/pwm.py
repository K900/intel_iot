import os.path

from libintel.util import gpio
from libintel.util.file import write_ignore_busy, read_file, write_file


class Pwm:
    _option_list = (
        'enabled',
        'duty_cycle',
        'period'
    )

    def __init__(self, pin_config):
        gpio.configure_out(pin_config["out_pin"], 1)
        gpio.configure_in(pin_config["pullup_pin"])

        conf = pin_config["pin_modes"]["PWM"]
        pwm_id = conf["pwm_id"]
        pwmchip_id = conf.get("pwmchip_id", 0)

        self._sysfs_root = "/sys/class/pwm/pwmchip{}/pwm{}/".format(pwmchip_id, pwm_id)
        write_ignore_busy("/sys/class/pwm/pwmchip{}/export".format(pwmchip_id), str(pwm_id))

    def _option_path(self, option):
        return os.path.join(self._sysfs_root, option)

    def __getattr__(self, item):
        if item in self._option_list:
            return read_file(self._option_path(item))
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key in self._option_list:
            write_file(self._option_path(key), str(value))
        else:
            raise AttributeError