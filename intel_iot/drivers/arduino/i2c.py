class EdisonArduinoI2c:
    """
    Intel Edison Arduino board I2C driver.
    This is here to delay loading the SMBus module until it's actually required, as it requires CFFI,
    which may not be present during runtime.
    """
    def bus(self):
        from smbus import SMBus
        return SMBus(6)