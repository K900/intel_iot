from intel_iot.board.generic import Board, GPIO_OUT, GPIO_IN, PWM
from intel_iot.drivers.generic.gpio import GpioIn, GpioOut
from intel_iot.drivers.generic.pwm import Pwm
from intel_iot.util import gpio as u_gpio


def make_pin(gpio, pwm=None):
    def setup_gpio(driver):
        u_gpio.set_mode(gpio, 0)
        return driver(gpio)

    conf = {
        GPIO_IN: lambda _: setup_gpio(GpioIn),
        GPIO_OUT: lambda _: setup_gpio(GpioOut)
    }

    if pwm:
        def setup_pwm(_):
            u_gpio.set_mode(gpio, 1)
            return Pwm(chip_id=0, pwm_id=pwm)

        conf[PWM] = setup_pwm

    return conf


PIN_CAPS = {
    "J17-1": make_pin(182, 2),
    "J17-5": make_pin(135),
    "J17-7": make_pin(27),
    "J17-8": make_pin(20),
    "J17-9": make_pin(28),
    "J17-10": make_pin(111),
    "J17-11": make_pin(109),
    "J17-12": make_pin(115),
    "J17-14": make_pin(128),
    "J18-1": make_pin(13, 1),
    "J18-2": make_pin(165),
    "J18-6": make_pin(19),
    "J18-7": make_pin(12, 0),
    "J18-8": make_pin(183, 3),
    "J18-10": make_pin(110),
    "J18-11": make_pin(114),
    "J18-12": make_pin(129),
    "J18-13": make_pin(130),
    "J19-4": make_pin(44),
    "J19-5": make_pin(46),
    "J19-6": make_pin(48),
    "J19-8": make_pin(131),
    "J19-9": make_pin(14),
    "J19-10": make_pin(40),
    "J19-11": make_pin(43),
    "J19-12": make_pin(77),
    "J19-13": make_pin(82),
    "J19-14": make_pin(83),
    "J20-4": make_pin(45),
    "J20-5": make_pin(47),
    "J20-6": make_pin(49),
    "J20-7": make_pin(15),
    "J20-8": make_pin(84),
    "J20-9": make_pin(42),
    "J20-10": make_pin(41),
    "J20-11": make_pin(78),
    "J20-12": make_pin(79),
    "J20-13": make_pin(80),
    "J20-14": make_pin(81)
}


class EdisonMiniBoard(Board):
    def _setup_i2c_pin(self, pin):
        self.setup(pin, GPIO_IN)
        u_gpio.set_mode(pin, 1)

    def setup_i2c_bus1(self):
        from smbus import SMBus

        self._setup_i2c_pin("J17-8")
        self._setup_i2c_pin("J18-6")

        return SMBus(1)

    def setup_i2c_bus6(self):
        from smbus import SMBus

        self._setup_i2c_pin("J17-7")
        self._setup_i2c_pin("J17-9")

        return SMBus(6)


board = EdisonMiniBoard(PIN_CAPS)
