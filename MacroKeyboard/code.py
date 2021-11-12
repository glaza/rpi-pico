# Sample application: https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse
# API Reference: https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode

import time
import board
from adafruit_hid.keycode import Keycode

from utils import send, sequence, write
from button import Button
from encoder import Encoder

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

buttons = [
    Encoder(  # Left Encoder
        "IDEA Debugging",
        board.GP4, board.GP5,
        send(Keycode.SHIFT, Keycode.F8), # Step Out of
        send(Keycode.F8)), # Step Over
    Encoder(  # Middle Encoder
        "macOS Change Workspaces",
        board.GP2, board.GP3,
        send(Keycode.CONTROL, Keycode.LEFT_ARROW),
        send(Keycode.CONTROL, Keycode.RIGHT_ARROW)),
    Encoder(  # Right Encoder
        "IDEA Move Up/Down",
        board.GP0, board.GP1,
        send(Keycode.CONTROL, Keycode.SHIFT, Keycode.UP_ARROW),
        send(Keycode.CONTROL, Keycode.SHIFT, Keycode.DOWN_ARROW)),

    Button(  # Left Encoder
        "IDEA Debugging Step Into",
        board.GP6,
        send(Keycode.F7)), # Step Into
    Button(  # Middle Encoder
        "macOS Expose",
        board.GP7,
        send(Keycode.CONTROL, Keycode.UP_ARROW)),
    Button(  # Right Encoder
        "IDEA Select More",
        board.GP22,
        send(Keycode.CONTROL, Keycode.W)),

    Button(  # Blue
        "IDEA Run Test",
        board.GP8,
        send(Keycode.CONTROL, Keycode.F5)),
    Button(  # Green
        "Long Press",
        board.GP9,
        sequence(
            send(Keycode.D),
            send(Keycode.O),
            send(Keycode.W),
            send(Keycode.N),
            send(Keycode.COMMA),
        ),
        sequence(
            send(Keycode.S),
            send(Keycode.H),
            send(Keycode.O),
            send(Keycode.R),
            send(Keycode.T),
            send(Keycode.COMMA),
        ),
        sequence(
            send(Keycode.L),
            send(Keycode.O),
            send(Keycode.N),
            send(Keycode.G),
            send(Keycode.COMMA),
        )),
    Button(  # White
        "Short only",
        board.GP10,
        send(Keycode.F5)),

    Button(  # Brown
        "IDEA Rename",
        board.GP11,
        send(Keycode.SHIFT, Keycode.F6)),
    Button(  # Clear
        "IDEA Comment",
        board.GP12,
        send(Keycode.CONTROL, Keycode.FORWARD_SLASH)),
    Button(  # Grey
        "Hello",
        board.GP13,
        write("Hello")),

    Button(  # Red
        "IDEA Extract Constant",
        board.GP14,
        send(Keycode.COMMAND, Keycode.CONTROL, Keycode.C)),
    Button(  # Silent Red
        "IDEA Inline",
        board.GP15,
        send(Keycode.COMMAND, Keycode.CONTROL, Keycode.N)),
    Button(  # Speed Silver
        "Slack Happy Face",
        board.GP16,
        write(":) "),
        send(Keycode.COMMAND, Keycode.ENTER)),

    Button(  # Black
        "IDEA Organize Imports",
        board.GP17,
        send(Keycode.COMMAND, Keycode.CONTROL, Keycode.O)),
    Button(  # Silent Black
        "IDEA Reformat Code",
        board.GP18,
        send(Keycode.COMMAND, Keycode.CONTROL, Keycode.L)),
    Button(  # RGB Silver
        "Slack Thumbs Up",
        board.GP19,
        write(":+1: "),
        send(Keycode.COMMAND, Keycode.ENTER))
]

while True:
    for button in buttons:
        button.detect()
