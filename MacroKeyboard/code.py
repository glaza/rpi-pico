# Sample application:
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse
# API Reference:
# https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode

import time
import board
from adafruit_hid.keycode import Keycode

from utils import noOp, send, write
from button import Button
from encoder import Encoder

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

buttons = [
    Encoder(  # Left Encoder
        "IDEA Debugging",
        board.GP4, board.GP5,
        send(Keycode.SHIFT, Keycode.F8),  # Step Out of
        send(Keycode.F8)),  # Step Over
    Encoder(  # Middle Encoder
        "Linux Change Workspaces",
        board.GP2, board.GP3,
        send(Keycode.ALT, Keycode.CONTROL, Keycode.LEFT_ARROW),
        send(Keycode.ALT, Keycode.CONTROL, Keycode.RIGHT_ARROW)),
    Encoder(  # Right Encoder
        "IDEA Move Up/Down",
        board.GP0, board.GP1,
        send(Keycode.CONTROL, Keycode.SHIFT, Keycode.UP_ARROW),
        send(Keycode.CONTROL, Keycode.SHIFT, Keycode.DOWN_ARROW)),

    Button(  # Left Encoder
        "IDEA Debugging Step Into",
        board.GP6,
        send(Keycode.F7)),  # Step Into
    Button(  # Middle Encoder
        "Linux Expose",
        board.GP7,
        send(Keycode.COMMAND)),
    Button(  # Right Encoder
        "IDEA Select More",
        board.GP22,
        send(Keycode.CONTROL, Keycode.W)),

    Button(  # Blue
        "IDEA Run Test",
        board.GP8,
        send(Keycode.CONTROL, Keycode.F5)),
    Button(  # Green
        "IDEA Comment",
        board.GP9,
        send(Keycode.CONTROL, Keycode.FORWARD_SLASH)),
    Button(  # White
        "Linux Lock Screen",
        board.GP10,
        send(Keycode.COMMAND, Keycode.L)),

    Button(  # Brown
        "IDEA Rename",
        board.GP11,
        send(Keycode.SHIFT, Keycode.F6)),
    Button(  # Clear
        "IDEA Go to Implementation/File Structure",
        board.GP12,
        noOp,  # Down
        send(Keycode.CONTROL, Keycode.ALT, Keycode.B),  # Short
        send(Keycode.CONTROL, Keycode.F12)),  # Long
    Button(  # Grey
        "Linux Screengrab",
        board.GP13,
        send(Keycode.SHIFT, Keycode.CONTROL, Keycode.PRINT_SCREEN)),

    Button(  # Red
        "IDEA Extract Constant/Method",
        board.GP14,
        noOp,  # Down
        send(Keycode.CONTROL, Keycode.ALT, Keycode.C),  # Short
        send(Keycode.CONTROL, Keycode.ALT, Keycode.M)),  # Long
    Button(  # Silent Red
        "IDEA Inline",
        board.GP15,
        send(Keycode.CONTROL, Keycode.ALT, Keycode.N)),
    Button(  # Speed Silver
        "Copy-Paste",
        board.GP16,
        send(Keycode.CONTROL, Keycode.C),
        send(Keycode.CONTROL, Keycode.V)),

    Button(  # Black
        "IDEA Organize Imports",
        board.GP17,
        send(Keycode.CONTROL, Keycode.ALT, Keycode.O)),
    Button(  # Silent Black
        "IDEA Reformat Code",
        board.GP18,
        send(Keycode.CONTROL, Keycode.ALT, Keycode.L)),
    Button(  # RGB Silver
        "Slack Thumbs Up",
        board.GP19,
        write(":+1: "),
        send(Keycode.CONTROL, Keycode.ENTER))
]

while True:
    for button in buttons:
        button.detect()
