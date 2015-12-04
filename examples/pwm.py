import time

from intel_iot.board.edison.arduino import board
from intel_iot.board.generic import PWM


def pwm():
    p = board.setup(3, PWM)

    p.duty_cycle = p.period // 2
    p.enabled = True

    time.sleep(0.2)

    p.duty_cycle = p.period // 4
    p.enabled = True  # reactivate after changing settings

    time.sleep(0.2)

    p.duty_cycle = p.period // 10
    p.enabled = True

    time.sleep(0.2)

    p.enabled = True
