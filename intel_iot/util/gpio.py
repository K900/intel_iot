import logging
import os.path

from intel_iot.util.file import write_ignore_busy, write_file, read_file

DIRECTION_IN = "in"
DIRECTION_OUT = "out"

log = logging.getLogger("intel_iot.util.gpio")


def _make_path(pin, option):
    return os.path.join("/sys/class/gpio/gpio{}/".format(pin), option)


def export(pin):
    log.debug("Exporting GPIO {}".format(pin))
    write_ignore_busy("/sys/class/gpio/export", str(pin))


def set_direction(pin, direction):
    log.debug("Setting GPIO {} to direction {}".format(pin, direction))
    write_file(_make_path(pin, 'direction'), direction)


def get_direction(pin):
    return read_file(_make_path(pin, 'direction'))


def get(pin):
    return int(read_file(_make_path(pin, 'value')))


# noinspection PyShadowingBuiltins
def set(pin, value):
    log.debug("Setting GPIO {} to value {}".format(pin, value))
    write_file(_make_path(pin, 'value'), str(value))


def set_mode(pin, mode):
    write_file("/sys/kernel/debug/gpio_debug/gpio{}/current_pinmux".format(pin),
               "mode{}".format(mode))

def configure_out(pin, value=0):
    export(pin)
    if value:
        direction = "high"
    else:
        direction = "low"
    set_direction(pin, direction)


def configure_in(pin):
    export(pin)
    set_direction(pin, DIRECTION_IN)
