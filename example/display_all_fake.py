'''
An example intended to be executed by CPython.

Instead of writing to an actual Neo7Segment device we use a 'fake'
NeoPixel strip (see PrintNeoPixel) to just print the RGB values of
each of the NeoPixels in the Neo7Segment.
'''
import time
from neo7segment import Neo7Segment, PrintNeoPixel

fake_neopixels = PrintNeoPixel(29)
neo7 = Neo7Segment(fake_neopixels, 1)

display_string = '1234567890.abcdef'
for char in display_string:
    neo7.display(char, (0, 0, 1))
    time.sleep(250 * 0.001)