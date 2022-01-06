import rotaryio
import usb_midi
import adafruit_midi  # MIDI protocol encoder/decoder library
from adafruit_midi.control_change import ControlChange
from utils import debug
from button import Button

USB_MIDI_CHANNEL = 1

class Dial:
    def __init__(
        self,
        name,
        ucPinLeft,
        ucPinRight,
        ucPinButton,
        channelDial,
        channelReset
    ):
        self.name = name
        self.rioEncoder = rotaryio.IncrementalEncoder(ucPinLeft, ucPinRight)
        self.button = Button(name + " button", ucPinButton, lambda: self.resetAll())
        self.midi = adafruit_midi.MIDI(
            midi_out=usb_midi.ports[1],
            out_channel=USB_MIDI_CHANNEL - 1,
        )
        self.channelDial = channelDial
        self.channelReset = channelReset
        self.resetPosition()

    def resetPosition(self):
        debug(self.name, "Reseting Position")
        self.rioEncoder.position = 63
        self.oldPosition = 63

    def resetChannel(self):
        debug(self.name, "Reseting Channel")
        self.midi.send(ControlChange(self.channelReset, 63))

    def resetAll(self):
        self.resetPosition()
        self.resetChannel()

    def detect(self):
        self.button.detect()
        if (self.oldPosition != self.rioEncoder.position):
            debug(self.name, "moved to", self.rioEncoder.position)
            value = min(127, max(0, self.rioEncoder.position))
            self.midi.send(ControlChange(self.channelDial, value))
            self.oldPosition = self.rioEncoder.position
