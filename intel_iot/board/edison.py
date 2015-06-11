from libintel.board.generic import Board
from libintel.pinmodes.analogue import Analogue
from libintel.pinmodes.gpio import GpioIn, GpioOut
from libintel.pinmodes.pwm import Pwm

ANALOGUE_DEPENDS = {
    10: "gpio_in",
    11: "gpio_in",
    12: "gpio_in",
    13: "gpio_in"
}

PIN_CONFIG = {
    "pre_mux": {
        214: 0
    },
    "post_mux": {
        214: 1
    },
    "pins": {
        0: {
            "gpio_pin": 130,
            "out_pin": 248,
            "pullup_pin": 216,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
            }
        },
        1: {
            "gpio_pin": 131,
            "out_pin": 249,
            "pullup_pin": 217,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
            }
        },
        2: {
            "gpio_pin": 128,
            "out_pin": 250,
            "pullup_pin": 218,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
            }
        },
        3: {
            "gpio_pin": 12,
            "out_pin": 251,
            "pullup_pin": 219,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
                "pwm": {
                    "class": Pwm,
                    "pin_mode": 1,
                    "pwm_id": 0
                }
            }
        },
        4: {
            "gpio_pin": 129,
            "out_pin": 252,
            "pullup_pin": 220,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
            }
        },
        5: {
            "gpio_pin": 13,
            "out_pin": 253,
            "pullup_pin": 221,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
                "pwm": {
                    "class": Pwm,
                    "pin_mode": 1,
                    "pwm_id": 1
                }
            }
        },
        6: {
            "gpio_pin": 182,
            "out_pin": 254,
            "pullup_pin": 222,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
                "pwm": {
                    "class": Pwm,
                    "pin_mode": 1,
                    "pwm_id": 2
                }
            }
        },
        7: {
            "gpio_pin": 48,
            "out_pin": 255,
            "pullup_pin": 223,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
            }
        },
        8: {
            "gpio_pin": 49,
            "out_pin": 256,
            "pullup_pin": 224,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
            }
        },
        9: {
            "gpio_pin": 183,
            "out_pin": 257,
            "pullup_pin": 225,

            "pin_modes": {
                "gpio_in": {"class": GpioIn},
                "gpio_out": {"class": GpioOut},
                "pwm": {
                    "class": Pwm,
                    "pin_mode": 1,
                    "pwm_id": 3
                }
            }
        },
        10: {
            "gpio_pin": 41,
            "out_pin": 258,
            "pullup_pin": 226,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        263: 1,
                        240: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        263: 1,
                        240: 0
                    }
                },
                "pwm": {
                    "class": Pwm,
                    "pin_mode": 1,
                    "pwm_id": 3,
                    "mux": {
                        263: 0
                    }
                }
            }
        },
        11: {
            "gpio_pin": 43,
            "out_pin": 259,
            "pullup_pin": 227,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        262: 1,
                        241: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        262: 1,
                        241: 0
                    }
                },
                "pwm": {
                    "class": Pwm,
                    "pin_mode": 1,
                    "pwm_id": 3,
                    "mux": {
                        262: 0
                    }
                }
            }
        },
        12: {
            "gpio_pin": 42,
            "out_pin": 260,
            "pullup_pin": 228,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        242: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        242: 0
                    }
                }
            }
        },
        13: {
            "gpio_pin": 40,
            "out_pin": 261,
            "pullup_pin": 229,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        243: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        243: 0
                    }
                }
            }
        },
        14: {
            "gpio_pin": 44,
            "out_pin": 232,
            "pullup_pin": 208,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        200: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        200: 0
                    }
                },
                "analogue": {
                    "class": Analogue,
                    "mux": {
                        200: 1
                    },
                    "depends": ANALOGUE_DEPENDS,
                    "channel": 0,
                }
            },
        },

        15: {
            "gpio_pin": 45,
            "out_pin": 233,
            "pullup_pin": 209,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        201: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        201: 0
                    }
                },
                "analogue": {
                    "class": Analogue,
                    "mux": {
                        201: 1
                    },
                    "depends": ANALOGUE_DEPENDS,
                    "channel": 1,
                }
            },
        },
        16: {
            "gpio_pin": 46,
            "out_pin": 234,
            "pullup_pin": 210,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        202: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        202: 0
                    }
                },
                "analogue": {
                    "class": Analogue,
                    "mux": {
                        202: 1
                    },
                    "depends": ANALOGUE_DEPENDS,
                    "channel": 2,
                }
            },
        },
        17: {
            "gpio_pin": 47,
            "out_pin": 235,
            "pullup_pin": 211,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        203: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        203: 0
                    }
                },
                "analogue": {
                    "class": Analogue,
                    "mux": {
                        203: 1
                    },
                    "depends": ANALOGUE_DEPENDS,
                    "channel": 3,
                }
            },
        },
        18: {
            "gpio_pin": 14,
            "out_pin": 236,
            "pullup_pin": 212,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        204: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        204: 0
                    }
                },
                "analogue": {
                    "class": Analogue,
                    "mux": {
                        204: 1
                    },
                    "depends": ANALOGUE_DEPENDS,
                    "channel": 4,
                }
            },
        },
        19: {
            "gpio_pin": 165,
            "out_pin": 237,
            "pullup_pin": 213,

            "pin_modes": {
                "gpio_in": {
                    "class": GpioIn,
                    "mux": {
                        205: 0
                    }
                },
                "gpio_out": {
                    "class": GpioOut,
                    "mux": {
                        205: 0
                    }
                },
                "analogue": {
                    "class": Analogue,
                    "mux": {
                        205: 1
                    },
                    "depends": ANALOGUE_DEPENDS,
                    "channel": 5,
                }
            },
        },
    },
}

board = Board(PIN_CONFIG)