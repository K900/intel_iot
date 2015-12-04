from functools import wraps

from intel_iot.board.generic import Board, GPIO_OUT, GPIO_IN, PWM, ADC, I2C
from intel_iot.drivers.generic.gpio import GpioOut
from intel_iot.drivers.generic.iiovoltage import IioVoltage
from intel_iot.drivers.generic.pwm import Pwm
from intel_iot.drivers.edison.arduino.gpio import EdisonArduinoGpioIn
from intel_iot.util.dicts import combine
from intel_iot.util import gpio as u_gpio

gpio_map = {
    # board pin -> (value, direction, pullup)
    0: (130, 248, 216),
    1: (131, 249, 217),
    2: (128, 250, 218),
    3: (12, 251, 219),
    4: (129, 252, 220),
    5: (13, 253, 221),
    6: (182, 254, 222),
    7: (48, 255, 223),
    8: (49, 256, 224),
    9: (183, 257, 225),
    10: (41, 258, 226),
    11: (43, 259, 227),
    12: (42, 260, 228),
    13: (40, 261, 229),
    14: (44, 232, 208),
    15: (45, 233, 209),
    16: (46, 234, 210),
    17: (47, 235, 211),
    18: (14, 236, 212),
    19: (165, 237, 213)
}


def ea_setup(func):
    @wraps(func)
    def wrapper(brd):
        u_gpio.set(214, 0),
        result = func(brd)
        u_gpio.set(214, 1)
        return result

    return wrapper


def setup_pin(pin, value_pin_mode, direction_value, mux):
    value, direction, pullup = gpio_map[pin]

    u_gpio.configure_in(pullup)
    u_gpio.configure_out(direction, direction_value)
    u_gpio.set_all(mux)
    u_gpio.set_mode(value, value_pin_mode)


def gpio(pin, mux=None):
    value, direction, pullup = gpio_map[pin]

    @ea_setup
    def setup_gpio_in(_):
        setup_pin(pin, 0, 0, mux)
        return EdisonArduinoGpioIn(value=value, direction=direction, pullup=pullup)

    @ea_setup
    def setup_gpio_out(_):
        setup_pin(pin, 0, 1, mux)
        return GpioOut(value)

    return {
        GPIO_IN: setup_gpio_in,
        GPIO_OUT: setup_gpio_out,
    }


def pwm(pin, pwm_id, mux=None):
    @ea_setup
    def setup_pwm(_):
        setup_pin(pin, 1, 1, mux)
        return Pwm(chip_id=0, pwm_id=pwm_id)

    return {
        PWM: setup_pwm
    }


def adc(pin, channel, mux=None):
    @ea_setup
    def setup_adc(brd):
        setup_pin(pin, 0, 0, mux)

        for dep in (10, 11, 12, 13):
            brd.setup(dep, GPIO_IN)

        return IioVoltage(device_id=1, channel=channel)

    return {
        ADC: setup_adc
    }


def i2c():
    def setup_i2c(brd):
        # noinspection PyPackageRequirements
        # noinspection PyUnresolvedReferences
        # Another optional dependency that doesn't even have to be installed.
        from smbus import SMBus

        u_gpio.set_all({
            204: 0,
            205: 0
        })

        def setup(pin):
            brd.setup(pin, GPIO_IN)
            u_gpio.set_mode(pin, 1)

        setup(18)
        setup(19)

        return SMBus(6)

    return {I2C: setup_i2c}

PIN_CAPS = {
    0: gpio(0),
    1: gpio(1),
    2: gpio(2),
    3: combine(
        gpio(2),
        pwm(3, pwm_id=0),
    ),
    4: gpio(4),
    5: combine(
        gpio(5),
        pwm(5, pwm_id=1),
    ),
    6: combine(
        gpio(6),
        pwm(6, pwm_id=2),
    ),
    7: gpio(7),
    8: gpio(8),
    9: combine(
        gpio(9),
        pwm(9, pwm_id=3),
    ),
    10: combine(
        gpio(10, mux={263: 1, 240: 0}),
        pwm(10, pwm_id=4, mux={263: 0}),
    ),
    11: combine(
        gpio(11, mux={262: 1, 241: 0}),
        pwm(11, pwm_id=5, mux={262: 0}),
    ),
    12: gpio(12, mux={242: 0}),
    13: gpio(13, mux={243: 0}),
    14: combine(
        gpio(14, mux={200: 0}),
        adc(14, channel=0, mux={200: 1}),
    ),
    15: combine(
        gpio(15, mux={201: 0}),
        adc(15, channel=1, mux={201: 1})
    ),
    16: combine(
        gpio(16, mux={202: 0}),
        adc(16, channel=2, mux={202: 0})
    ),
    17: combine(
        gpio(17, mux={203: 0}),
        adc(17, channel=3, mux={203: 1}),
    ),
    18: combine(
        gpio(18, mux={204: 0}),
        adc(18, channel=4, mux={204: 1}),
        i2c(),
    ),
    19: combine(
        gpio(19, mux={205: 0}),
        adc(19, channel=4, mux={205: 1}),
        i2c(),
    )
}
# I2C: {
#     "mux": {204: 0, 205: 0},
#     "depends": {18: I2C, 19: I2C}
# }
# bus 6

# Pin aliases
A0 = 14
A1 = 15
A2 = 16
A3 = 17
A4 = 18
A5 = 19

board = Board(PIN_CAPS)
