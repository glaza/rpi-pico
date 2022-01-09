import time
import board
from dial import Dial

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

dials = [
    Dial("Exposure", board.GP0, board.GP1, board.GP2, 1, 2),
]

while True:
    for dial in dials:
        dial.detect()
