
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

verbose = True
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

def debug(*messages):
    if verbose:
        print(messages)

def smallPause():
    return lambda: time.sleep(0.01)

def mediumPause():
    return lambda: time.sleep(0.1)

def noOp():
    return None

def send(*keys):
    '''returns a lambda that sends the requested keys'''        
    return lambda: keyboard.send(*keys)

def write(string):
    '''returns a lambda that writes the requested string on a US keyboard layout'''
    return lambda: keyboard_layout.write(string)

def sequence(*strokes):
    '''returns a lambda that calls the given lambdas in a sequence'''
    return lambda: applyAll(*strokes)

def applyAll(*lambs):
    for lamb in lambs:
        lamb()

