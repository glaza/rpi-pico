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
        # print(self.rioEncoder.position)
        self.fnLeft = fnLeft
        self.fnRight = fnRight

    def detect(self):
        if (self.position != self.rioEncoder.position):
            # print(self.rioEncoder.position)
            pass
        if self.rioEncoder.position > self.position:
            self.fnRight()
        elif self.rioEncoder.position < self.position:
            self.fnLeft()
        self.position = self.rioEncoder.position

buttons = [
    Encoder(board.GP0, send(Keycode.LEFT_ARROW),
            board.GP1, send(Keycode.RIGHT_ARROW)),
    Encoder(board.GP2, send(Keycode.CONTROL, Keycode.LEFT_ARROW),
            board.GP3, send(Keycode.CONTROL, Keycode.RIGHT_ARROW)),
    Encoder(board.GP4, send(Keycode.LEFT_ARROW),
            board.GP5, send(Keycode.RIGHT_ARROW)),
    Button(board.GP6, send(Keycode.FIVE)),  # Right Encoder
    Button(board.GP7, send(Keycode.CONTROL, Keycode.UP_ARROW)),  # Middle Encoder
    Button(board.GP22, send(Keycode.TWO, Keycode.TWO)),  # Left Encoder
    Button(board.GP8, send(Keycode.EIGHT)),
    Button(board.GP9, send(Keycode.NINE)),
    Button(board.GP10, send(Keycode.ONE, Keycode.ZERO)),
    Button(board.GP11, send(Keycode.ONE, Keycode.ONE)),
    Button(board.GP12, send(Keycode.ONE, Keycode.TWO)),
    Button(board.GP13, send(Keycode.ONE, Keycode.THREE)),
    Button(board.GP14, send(Keycode.ONE, Keycode.FOUR)),
    Button(board.GP15, send(Keycode.ONE, Keycode.FIVE)),
    Button(board.GP16, send(Keycode.ONE, Keycode.SIX)),
    Button(board.GP17, send(Keycode.ONE, Keycode.SEVEN)),
    Button(board.GP18, send(Keycode.ONE, Keycode.EIGHT)),
    Button(board.GP19, send(Keycode.ONE, Keycode.NINE)),
]
# 
while True:
    time.sleep(0.01)
    for button in buttons:
        button.detect()
