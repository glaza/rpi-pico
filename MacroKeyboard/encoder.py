
import rotaryio
from utils import debug

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
