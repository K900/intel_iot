Unofficial library for interfacing with Intel IoT hardware based on the Quark SoC from Python 3 on Linux. Handles GPIO multiplexing and all other black magic required to make things _just work_.

Born out of frustration with libmraa (hi `MRAA_ERROR_INVALID_RESOURCE`).

## Disclaimer
Everything is unstable and will break, so please don't use this in production. We take no responsibility for bricked hardware or any other damage using this library may have caused.

However, it has been tested on multiple small projects and seems to work properly.

## Goals
* Object oriented, pythonic API
* Easy configuration
* libmraa feature parity on supported hardware
* No footguns

## Current features
* Generic board configuration format
* GPIO input/output
* ADC input
* PWM output

## Supported hardware
* Intel Edison Arduino breakout board

## Limitations
* I2C / SPI support is WIP (and will probably need a C extension)
* No other hardware is supported as of now (Galileo Gen1 and Edison small breakout boards possible, we don't have any other hardware)
* Some things may be inadvertently hardcoded to support the Edison Arduino board only
* Documentation doesn't exist

## Non-goals
* Very high performance
* libmraa API compatibility
* Python 2 support
* OS X / Windows support

## References
* [libmraa](https://github.com/intel-iot-devkit/mraa) - mostly the source code, as the documentation is severely lacking
* [Edison GPIO pin multiplexing guide](http://www.emutexlabs.com/project/215-intel-edison-gpio-pin-multiplexing-guide)
* [Edison Arduino board hardware guide](https://communities.intel.com/servlet/JiveServlet/downloadBody/23161-102-8-27954/edison-arduino_HG_331191-005.pdf)