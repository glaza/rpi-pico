# Sample application:
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse
# API Reference:
# https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode

import time
import board
from adafruit_hid.keycode import Keycode

from utils import noOp, send, write, sequence
from button import Button
from encoder import Encoder

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

useLinux = False  # False for macOs

def linux(lamb):
    return lamb if useLinux else noOp

def macOs(lamb):
    return lamb if not useLinux else noOp

buttons = [
    # ####################### Encoders ########################
    Encoder(  # Left Encoder
        "IDEA Debugging",
        board.GP4, board.GP5,
        send(Keycode.SHIFT, Keycode.F8),  # Step Out of
        send(Keycode.F8),
    ),  # Step Over
    Encoder(  # Middle Encoder
        "OS Change Workspaces",
        board.GP2, board.GP3,
        sequence(
            linux(send(Keycode.ALT, Keycode.CONTROL, Keycode.LEFT_ARROW)),
            macOs(send(Keycode.CONTROL, Keycode.LEFT_ARROW)),
        ),
        sequence(
            linux(send(Keycode.ALT, Keycode.CONTROL, Keycode.RIGHT_ARROW)),
            macOs(send(Keycode.CONTROL, Keycode.RIGHT_ARROW)),
        ),
    ),
    Encoder(  # Right Encoder
        "IDEA Move Up/Down",
        board.GP0, board.GP1,
        send(Keycode.CONTROL, Keycode.SHIFT, Keycode.UP_ARROW),
        send(Keycode.CONTROL, Keycode.SHIFT, Keycode.DOWN_ARROW),
    ),

    Button(  # Left Encoder
        "IDEA Debugging Step Into",
        board.GP6,
        send(Keycode.F7),
    ),  # Step Into
    Button(  # Middle Encoder
        "OS Expose",
        board.GP7,
        sequence(
            linux(send(Keycode.COMMAND)),
            macOs(send(Keycode.CONTROL, Keycode.UP_ARROW)),
        ),
    ),
    Button(  # Right Encoder
        "IDEA Select More",
        board.GP22,
        send(Keycode.CONTROL, Keycode.W)
    ),

    # ####################### Clicky ########################
    Button(  # Blue
        "IDEA Run Test",
        board.GP8,
        sequence(
            linux(send(Keycode.CONTROL, Keycode.F5)),
            macOs(send(Keycode.COMMAND, Keycode.F5)),
        ),
    ),
    Button(  # Green
        "IDEA Comment",
        board.GP9,
        sequence(
            linux(send(Keycode.CONTROL, Keycode.FORWARD_SLASH)),
            macOs(send(Keycode.COMMAND, Keycode.FORWARD_SLASH)),
        ),
    ),
    Button(  # White
        "Linux Lock Screen",
        board.GP10,
        send(Keycode.COMMAND, Keycode.L)),
    
    # ####################### Tacktile ########################
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
        "Screengrab",
        board.GP13,
        sequence(
            linux(send(Keycode.SHIFT, Keycode.CONTROL, Keycode.PRINT_SCREEN)),
            macOs(send(Keycode.COMMAND, Keycode.SHIFT, Keycode.FOUR)),
        ),
    ),

    # ####################### Red Linear ########################
    Button(  # Red
        "IDEA Extract Constant/Method",
        board.GP14,
        noOp,  # Down
        sequence(  # Short
            linux(send(Keycode.CONTROL, Keycode.ALT, Keycode.C)),
            macOs(send(Keycode.COMMAND, Keycode.ALT, Keycode.C)),
        ),
        sequence(  # Long
            linux(send(Keycode.CONTROL, Keycode.ALT, Keycode.M)),
            macOs(send(Keycode.COMMAND, Keycode.ALT, Keycode.M)),
        ),
    ),
    Button(  # Silent Red
        "OS Paste",
        board.GP15,
        sequence(
            linux(send(Keycode.CONTROL, Keycode.V)),
            macOs(send(Keycode.COMMAND, Keycode.V)),
        ),
    ),
    Button(  # Speed Silver
        "OS Copy/Cut",
        board.GP16,
        noOp,
        sequence(  # Short
            linux(send(Keycode.CONTROL, Keycode.C)),
            macOs(send(Keycode.COMMAND, Keycode.C)),
        ),
        sequence(  # Long
            linux(send(Keycode.CONTROL, Keycode.X)),
            macOs(send(Keycode.COMMAND, Keycode.X)),
        ),
    ),

    # ####################### Black Linear ########################
    Button(  # Black
        "IDEA Organize Imports",
        board.GP17,
        sequence(
            linux(send(Keycode.CONTROL, Keycode.ALT, Keycode.O)),
            macOs(send(Keycode.SHIFT, Keycode.ALT, Keycode.O)),
        ),
    ),
    Button(  # Silent Black
        "IDEA Reformat Code",
        board.GP18,
        sequence(
            linux(send(Keycode.CONTROL, Keycode.ALT, Keycode.L)),
            macOs(send(Keycode.COMMAND, Keycode.ALT, Keycode.L)),
        ),
    ),
    Button(  # RGB Silver
        "Slack Thumbs Up",
        board.GP19,
        write(":+1: "),  # Down
        sequence(  # Up
            linux(send(Keycode.CONTROL, Keycode.ENTER)),
            macOs(send(Keycode.COMMAND, Keycode.ENTER)),
        ),
    )
]

while True:
    for button in buttons:
        button.detect()
