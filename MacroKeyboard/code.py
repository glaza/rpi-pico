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
verbose = False

def debug(*messages):
    if verbose:
        print(messages)

def noOp():
    return None

def send(*keys):
    '''returns a lambda that sends the requested keys'''
    return lambda: keyboard.send(*keys)

def sequence(*strokes):
    '''returns a lambda that calls the given lambdas in a sequence'''
    return lambda: applyAll(*strokes)

def applyAll(*lambs):
    for lamb in lambs:
        lamb()

class Button:
    def __init__(self, name, ucPin, fnDown=noOp, fnUp=noOp):
        '''
        ucPin: microcontroller.Pin
        fnDown: lambda or function to be invoked when button is pressed
        fnUp: lambda or function to be invoked when button is depressed
        '''
        self.name = name
        self.ucPin = ucPin
        self.ioPin = digitalio.DigitalInOut(ucPin)
        self.ioPin.direction = digitalio.Direction.INPUT
        self.ioPin.pull = digitalio.Pull.UP
        self.value = True
        self.fnDown = fnDown
        self.fnUp = fnUp

    def detect(self):
        if self.value and not self.ioPin.value:
            debug(self.name, "pressed")
            self.fnDown()

        elif not self.value and self.ioPin.value:
            debug(self.name, "released")
            self.fnUp()

        self.value = self.ioPin.value

class Encoder:
    def __init__(self, name, ucPinLeft, ucPinRight, fnLeft, fnRight):
        self.name = name
        self.rioEncoder = rotaryio.IncrementalEncoder(ucPinLeft, ucPinRight)
        self.position = self.rioEncoder.position
        self.fnLeft = fnLeft
        self.fnRight = fnRight

    def detect(self):
        if (self.position != self.rioEncoder.position):
            pass
        if self.rioEncoder.position > self.position:
            debug(self.name, "right")
            self.fnRight()
        elif self.rioEncoder.position < self.position:
            debug(self.name, "left")
            self.fnLeft()
        self.position = self.rioEncoder.position

buttons = [
    Encoder(  # Right Encoder
        "",
        board.GP0, board.GP1,
        send(Keycode.LEFT_ARROW),
        send(Keycode.RIGHT_ARROW)),
    Encoder(  # Middle Encoder
        "Change Workspaces",
        board.GP2, board.GP3,
        send(Keycode.CONTROL, Keycode.LEFT_ARROW),
        send(Keycode.CONTROL, Keycode.RIGHT_ARROW)),
    Encoder(  # Left Encoder
        "",
        board.GP4, board.GP5,
        send(Keycode.LEFT_ARROW),
        send(Keycode.RIGHT_ARROW)),
        
    Button(  # Right Encoder
        "", board.GP6, send(Keycode.FIVE)),
    Button(  # Middle Encoder
        "", board.GP7, send(Keycode.CONTROL, Keycode.UP_ARROW)),
    Button(  # Left Encoder 
        "", board.GP22, send(Keycode.TWO, Keycode.TWO)),
        
    Button(  # Blue
        "", board.GP8, send(Keycode.EIGHT)),
    Button(  # Green
        "", board.GP9, send(Keycode.NINE)),
    Button(  # White
        "", board.GP10, send(Keycode.ONE, Keycode.ZERO)),
    
    Button(  # Brown
        "", board.GP11, send(Keycode.ONE, Keycode.ONE)),
    Button(  # Clear
        "", board.GP12, send(Keycode.ONE, Keycode.TWO)),
    Button(  # Grey
        "", board.GP13, send(Keycode.ONE, Keycode.THREE)),
    
    Button(  # Red
        "", board.GP14, send(Keycode.ONE, Keycode.FOUR)),
    Button(  # Silent Red
        "", board.GP15, send(Keycode.ONE, Keycode.FIVE)),
    Button(  # Speed Silver
        "", board.GP16, send(Keycode.ONE, Keycode.SIX)),
    
    Button(  # Black
        "", board.GP17, send(Keycode.COMMAND, Keycode.CONTROL, Keycode.O)),
    Button(  # Silent Black
        "", board.GP18, send(Keycode.ONE, Keycode.EIGHT)),
    Button(  # RGB Silver
        "Slack Thumbs Up",
        board.GP19,
        sequence(
            send(Keycode.SHIFT, Keycode.SEMICOLON),
            send(Keycode.SHIFT, Keycode.EQUALS),
            send(Keycode.ONE),
            send(Keycode.SHIFT, Keycode.SEMICOLON),
            send(Keycode.SPACE)
        )
    )
]

while True:
    time.sleep(0.01)
    for button in buttons:
        button.detect()
