#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2024 Miodrag Milanovic <mmicko@gmail.com>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.nanoxplore import NanoXplorePlatform

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk / Rst
    ("clk25", 0, Pins("IOB10_D09P"), IOStandard("LVCMOS")),
    #("rst",   0, Pins(""), IOStandard("LVCMOS")),

    # Buttons
    ("user_btn", 0, Pins("IOB7_D08"), IOStandard("LVCMOS")),
    ("user_btn", 1, Pins("IOB7_D09"), IOStandard("LVCMOS")),
    ("user_btn", 2, Pins("IOB7_D10"), IOStandard("LVCMOS")),
    ("user_btn", 3, Pins("IOB7_D11"), IOStandard("LVCMOS")),
    ("user_btn", 4, Pins("IOB7_D12"), IOStandard("LVCMOS")),
    ("user_btn", 5, Pins("IOB7_D13"), IOStandard("LVCMOS")),
    ("user_btn", 6, Pins("IOB7_D14"), IOStandard("LVCMOS")),
    ("user_btn", 7, Pins("IOB7_D15"), IOStandard("LVCMOS")),

    # Leds
    ("user_led", 0, Pins("IOB7_D16"), IOStandard("LVCMOS")),
    ("user_led", 1, Pins("IOB7_D17"), IOStandard("LVCMOS")),
    ("user_led", 2, Pins("IOB7_D18"), IOStandard("LVCMOS")),
    ("user_led", 3, Pins("IOB7_D19"), IOStandard("LVCMOS")),
    ("user_led", 4, Pins("IOB7_D20"), IOStandard("LVCMOS")),
    ("user_led", 5, Pins("IOB7_D21"), IOStandard("LVCMOS")),
    ("user_led", 6, Pins("IOB7_D22"), IOStandard("LVCMOS")),
    ("user_led", 7, Pins("IOB7_D23"), IOStandard("LVCMOS")),

    # Serial
    ("serial", 0,
        Subsignal("tx", Pins("IOB1_D01"), IOStandard("LVCMOS")),
        Subsignal("rx", Pins("IOB1_D00"), IOStandard("LVCMOS"))
    ),
]

# Connectors ---------------------------------------------------------------------------------------

_connectors = []

# Platform -----------------------------------------------------------------------------------------

class Platform(NanoXplorePlatform):
    def __init__(self, toolchain="impulse"):
        NanoXplorePlatform.__init__(self, "NG-ULTRA", _io,  _connectors, toolchain=toolchain)

    def create_programmer(self):
        return NanoXplorePlatform()

    def do_finalize(self, fragment):
        NanoXplorePlatform.do_finalize(self, fragment)
