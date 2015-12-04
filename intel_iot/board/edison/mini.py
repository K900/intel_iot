from intel_iot.board.generic import Board, GPIO_OUT, GPIO_IN, PWM, I2C
from intel_iot.drivers.generic.gpio import GpioIn, GpioOut
from intel_iot.drivers.generic.pwm import Pwm
from intel_iot.util import gpio as u_gpio
from intel_iot.util.dicts import combine


def gpio(number):
    def setup_gpio(driver):
        u_gpio.set_mode(number, 0)
        return driver(number)

    return {
        GPIO_IN: lambda _: setup_gpio(GpioIn),
        GPIO_OUT: lambda _: setup_gpio(GpioOut)
    }


def pwm(number):
    def setup_pwm(_):
        u_gpio.set_mode(gpio, 1)
        return Pwm(chip_id=0, pwm_id=number)

    return {PWM: setup_pwm}


def i2c():
    def setup_i2c(brd):
        # noinspection PyPackageRequirements
        # noinspection PyUnresolvedReferences
        # Another optional dependency that doesn't even have to be installed.
        from smbus import SMBus

        def setup(pin):
            brd.setup(pin, GPIO_IN)
            u_gpio.set_mode(pin, 1)

        setup("J17-7")
        setup("J17-9")

        return SMBus(6)

    return {I2C: setup_i2c}


PIN_CAPS = {
    "J17-1": combine(
        gpio(182),
        pwm(2)
    ),
    "J17-5": gpio(135),
    "J17-7": combine(
        gpio(27),
        i2c()
    ),
    "J17-8": gpio(20),
    "J17-9": combine(
        gpio(28),
        i2c()
    ),
    "J17-10": gpio(111),
    "J17-11": gpio(109),
    "J17-12": gpio(115),
    "J17-14": gpio(128),
    "J18-1": combine(
        gpio(13),
        pwm(1)
    ),
    "J18-2": gpio(165),
    "J18-6": gpio(19),
    "J18-7": combine(
        gpio(12),
        pwm(0)
    ),
    "J18-8": combine(
        gpio(183),
        pwm(3)
    ),
    "J18-10": gpio(110),
    "J18-11": gpio(114),
    "J18-12": gpio(129),
    "J18-13": gpio(130),
    "J19-4": gpio(44),
    "J19-5": gpio(46),
    "J19-6": gpio(48),
    "J19-8": gpio(131),
    "J19-9": gpio(14),
    "J19-10": gpio(40),
    "J19-11": gpio(43),
    "J19-12": gpio(77),
    "J19-13": gpio(82),
    "J19-14": gpio(83),
    "J20-4": gpio(45),
    "J20-5": gpio(47),
    "J20-6": gpio(49),
    "J20-7": gpio(15),
    "J20-8": gpio(84),
    "J20-9": gpio(42),
    "J20-10": gpio(41),
    "J20-11": gpio(78),
    "J20-12": gpio(79),
    "J20-13": gpio(80),
    "J20-14": gpio(81)
}

board = Board(PIN_CAPS)
