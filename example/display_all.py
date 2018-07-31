'''
An example intended to be executed on a board running MicroPython with the
control line of the Neo7Segment on Pin(17).
'''
import utime as time
from neopixel import NeoPixel
from machine import Pin

# Note that the timing parameter is only required for ESP32. See:
#   https://github.com/micropython/micropython-esp32/issues/159
neo = NeoPixel(Pin(17), 29, timing=True)
neo7 = Neo7Segment(neo, 1)

display_string = '1234567890.abcdef'
for char in display_string:
    neo7.display(char, (0, 0, 1))
    time.sleep_ms(250)