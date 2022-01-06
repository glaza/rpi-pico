import time
import board
import usb_midi
import adafruit_midi  # MIDI protocol encoder/decoder library
from adafruit_midi.control_change import ControlChange
from utils import noOp
from button import Button
from encoder import Encoder

USB_MIDI_channel = 1
usb_midi = adafruit_midi.MIDI(
    midi_out=usb_midi.ports[1], out_channel=USB_MIDI_channel - 1
)

def midi_send(position):
    value = (position + 63) % 127
    usb_midi.send(ControlChange(1, value))

def midi():
    return lambda position: midi_send(position)

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

buttons = [
    Encoder(
        "IDEA Move Up/Down",
        board.GP0, board.GP1,
        midi(),
        midi(),
    ),

    Button(
        "IDEA Debugging Step Into",
        board.GP2,
        noOp(),
    ),
]

while True:
    for button in buttons:
        button.detect()
