import logging
import os.path
from functools import wraps
from intel_iot.util.file import write_ignore_busy, write_file, read_file

DIRECTION_IN = "in"
DIRECTION_OUT = "out"

log = logging.getLogger("intel_iot.util.gpio")


def _make_path(pin, option):
    return os.path.join("/sys/class/gpio/gpio{}/".format(pin), option)


def export(gpio):
    log.debug("Exporting GPIO {}".format(gpio))
    write_ignore_busy("/sys/class/gpio/export", str(gpio))


def export_if_not_found(func):
    @wraps(func)
    def wrapper(gpio, *args, **kwargs):
        try:
            return func(gpio, *args, **kwargs)
        except IOError:
            export(gpio)
            return func(gpio, *args, **kwargs)

    return wrapper


@export_if_not_found
def get(gpio):
    return int(read_file(_make_path(gpio, 'value')))


# noinspection PyShadowingBuiltins
@export_if_not_found
def set(gpio, value):
    log.debug("Setting GPIO {} to value {}".format(gpio, value))
    write_file(_make_path(gpio, 'value'), str(value))


def set_all(values):
    if values:
        for gpio, value in values.items():
            configure_out(gpio, value)


@export_if_not_found
def get_direction(gpio):
    return read_file(_make_path(gpio, 'direction'))


@export_if_not_found
def set_direction(gpio, direction):
    log.debug("Setting GPIO {} to direction {}".format(gpio, direction))
    write_file(_make_path(gpio, 'direction'), direction)


@export_if_not_found
def set_mode(gpio, mode):
    write_file("/sys/kernel/debug/gpio_debug/gpio{}/current_pinmux".format(gpio),
               "mode{}".format(mode))


@export_if_not_found
def configure_out(gpio, value=0):
    if value:
        direction = "high"
    else:
        direction = "low"
    set_direction(gpio, direction)


@export_if_not_found
def configure_in(pin):
    set_direction(pin, DIRECTION_IN)
