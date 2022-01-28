import time
import board
from adafruit_hid.keycode import Keycode
from button import Button
from dial import Dial
# from encoder import Encoder
from utils import send

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

dials = [
    Dial("Exposure", board.GP0, board.GP1, board.GP2, 1, 2),
    Dial("Contrast", board.GP3, board.GP4, board.GP5, 3, 4),
    Dial("Highlights", board.GP6, board.GP7, board.GP8, 5, 6),
    Dial("Shadows", board.GP9, board.GP10, board.GP11, 7, 8),
    Dial("Whites", board.GP14, board.GP15, board.GP16, 9, 10),
    Dial("Blacks", board.GP17, board.GP18, board.GP19, 11, 12),
    Dial("Vibrance", board.GP20, board.GP21, board.GP22, 13, 14),
    Dial("Saturation", board.GP26, board.GP27, board.GP28, 15, 16),
    # # Sadly, the 9th encoder max's out the PIOs :(
    # Encoder("Next/Prev", board.GP12, board.GP13,
    #         send(Keycode.LEFT_ARROW), send(Keycode.RIGHT_ARROW)),
    Button("Next", board.GP12, send(Keycode.RIGHT_ARROW)),
    Button("Prev", board.GP13, send(Keycode.LEFT_ARROW)),
]

while True:
    for dial in dials:
        dial.detect()
