# Documentation: https://github.com/glaza/rpi-pico

import time
import board
from adafruit_hid.keycode import Keycode

from utils import send
from button import Button
from encoder import Encoder

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

buttons = [
    # ####################### Head ########################
    Encoder(  # Encoder
        "IDEA Move Block",
        board.GP26, board.GP27,
        send(Keycode.LEFT_ARROW),
        send(Keycode.RIGHT_ARROW),
    ),
    Button(  # Encoder's Button
        "IDEA Select Block",
        board.GP28,
        send(Keycode.ZERO),
    ),

    # ####################### Left ########################
    Button(
        "Left Top",
        board.GP1,
        send(Keycode.ONE),
    ),
    Button(
        "Left Middle",
        board.GP5,
        send(Keycode.TWO),
    ),
    Button(
        "Left Bottom",
        board.GP9,
        send(Keycode.THREE),
    ),

    # ####################### Right ########################
    Button(
        "Right Top",
        board.GP22,
        send(Keycode.FOUR),
    ),
    Button(
        "Right Middle",
        board.GP18,
        send(Keycode.FIVE),
    ),
    Button(
        "Right Bottom",
        board.GP14,
        send(Keycode.SIX),
    ),
]

while True:
    for button in buttons:
        button.detect()
