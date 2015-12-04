from intel_iot.board.edison.arduino import board, A1
from intel_iot.board.generic import ADC


def adc():
    a = board.setup(A1, ADC)
    while True:
        print("ADC value: {:4}\r".format(a.value))
