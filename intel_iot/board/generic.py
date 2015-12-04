# Pin mode constants
GPIO_IN = "gpio_in"
GPIO_OUT = "gpio_out"
ADC = "adc"
PWM = "pwm"
I2C = "i2c"


class Board:
    """
    Generic class for interfacing with a development board.
    """

    def setup(self, pin, mode):
        """
        Sets up a pin header for a specified interaction mode, then returns an object providing an API for it.
        :param pin: Pin number/ID on the development board.
        :param mode: I/O configuration to use, e.g. GPIO input, PWM output, etc.
        :return: Wrapper ('driver') object for the specified configuration.
        """

        return self._capabilities[pin][mode](self)

    def __init__(self, capabilities):
        """
        Creates a new Board instance based on the configuration object supplied by the caller.
        This shouldn't be used directly unless you are writing a board configuration module.
        Board configuration modules should export an instance of this class as a module level variable.
        :param capabilities: The configuration object describing the board.
        :return: The finished Board object.
        """
        self._capabilities = capabilities
