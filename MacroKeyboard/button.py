
import digitalio
from utils import noOp, debug

LONG_PRESS = 100  # Cycles

class Button:
    def __init__(self, name, ucPin, fnDown=noOp, fnShortUp=noOp, fnLongUp=None):
        '''
        ucPin: microcontroller.Pin
        fnDown: lambda or function to be invoked when button is pressed
        fnShortUp: lambda or function to be invoked when button is depressed quickly
        fnLongUp: lambda or function to be invoked when button is depressed slowly
        '''
        self.name = name
        self.ucPin = ucPin
        self.ioPin = digitalio.DigitalInOut(ucPin)
        self.ioPin.direction = digitalio.Direction.INPUT
        self.ioPin.pull = digitalio.Pull.UP
        self.value = True
        self.fnDown = fnDown
        self.fnShortUp = fnShortUp
        self.fnLongUp = fnLongUp
        self.downCount = 0

    def detect(self):
        oldButton = not self.value
        newButton = not self.ioPin.value

        if not oldButton and newButton:
            debug(self.name, "pressed")
            self.fnDown()

        if oldButton:
            self.downCount += 1

            if not newButton:
                self.up()
                self.downCount = 0

        self.value = self.ioPin.value

    def up(self):
        if self.fnLongUp and self.downCount > LONG_PRESS:
            debug(self.name, "released slowly", self.downCount)
            self.fnLongUp()
        else:
            debug(self.name, "released", self.downCount)
            self.fnShortUp()
