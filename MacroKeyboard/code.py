# https://circuitpython.readthedocs.io/en/6.2.x/README.html
# https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html
import time

import board
import digitalio
import rotaryio
import usb_hid
from adafruit_hid.keyboard import Keyboard
# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

keyboard = Keyboard(usb_hid.devices)

def noOp():
    return None

def send(*keys):
    '''returns a lambda that sends the requested keys'''
    return lambda: keyboard.send(*keys)

class Button:
    def __init__(self, ucPin, fnDown=noOp, fnUp=noOp):
        '''
        ucPin: microcontroller.Pin
        fnDown: lambda or function to be invoked when button is pressed
        fnUp: lambda or function to be invoked when button is depressed
        '''
        self.ucPin = ucPin
        self.ioPin = digitalio.DigitalInOut(ucPin)
        self.ioPin.direction = digitalio.Direction.INPUT
        self.ioPin.pull = digitalio.Pull.UP
        self.value = True
        self.fnDown = fnDown
        self.fnUp = fnUp

    def detect(self):
        if self.value and not self.ioPin.value:
            self.fnDown()

        elif not self.value and self.ioPin.value:
            self.fnUp()

        self.value = self.ioPin.value

class Encoder:
    def __init__(self, ucPinLeft, fnLeft, ucPinRight, fnRight):
        self.rioEncoder = rotaryio.IncrementalEncoder(ucPinLeft, ucPinRight)
        self.position = self.rioEncoder.position
        print(self.rioEncoder.position)
        self.fnLeft = fnLeft
        self.fnRight = fnRight

    def detect(self):
        if (self.position != self.rioEncoder.position):
            print(self.rioEncoder.position)
        if self.rioEncoder.position > self.position:
            self.fnRight()
        elif self.rioEncoder.position < self.position:
            self.fnLeft()
        self.position = self.rioEncoder.position

buttons = [
    Button(board.GP16, send(Keycode.ZERO)),  # Encoder
    Encoder(board.GP0, send(Keycode.LEFT_ARROW),
            board.GP1, send(Keycode.RIGHT_ARROW)),
    Encoder(board.GP2, send(Keycode.LEFT_ARROW),
            board.GP3, send(Keycode.RIGHT_ARROW)),
    Encoder(board.GP4, send(Keycode.LEFT_ARROW),
            board.GP5, send(Keycode.RIGHT_ARROW)),
    Button(board.GP20, send(Keycode.THREE)),
    Button(board.GP21, send(Keycode.FOUR)),
    Button(board.GP22, send(Keycode.FIVE)),
    Button(board.GP15, send(Keycode.K)),
]

while True:
    time.sleep(0.01)
    for button in buttons:
        button.detect()
