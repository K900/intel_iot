import time

from intel_iot.board.edison.arduino import board
from intel_iot.board.generic import GPIO_OUT, GPIO_IN


def blink():
    led = board.setup(7, GPIO_OUT)
    for _ in range(5):
        led.value = 1
        time.sleep(0.2)
        led.value = 0
        time.sleep(0.2)


def read():
    pin = board.setup(7, GPIO_IN)
    print(pin.value)


def read_pullup():
    pin = board.setup(7, GPIO_IN)

    # enable pullup resistors (Edison Arduino board only)
    pin.pullup = True

    print(pin.value)
