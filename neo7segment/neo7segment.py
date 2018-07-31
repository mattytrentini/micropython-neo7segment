try:
    from itertools import chain
except ImportError:
    # itertools is an external dependency in MicroPython
    # See: https://github.com/micropython/micropython-lib/tree/master/itertools
    # Only chain is required so can just define it here
    def chain(*p):
        for i in p:
            yield from i

TOP = range(4)
TOP_LEFT = range(20,24)
TOP_RIGHT = range(4,8)
MIDDLE = range(24, 28)
BOTTOM_LEFT = range(16,20)
BOTTOM_RIGHT = range(8,12)
BOTTOM = range(12,16)
DOT = [28]

char_to_segment = {'0': list(chain(TOP, TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM)),
                   '1': list(chain(TOP_RIGHT, BOTTOM_RIGHT)),
                   '2': list(chain(TOP, TOP_RIGHT, MIDDLE, BOTTOM_LEFT, BOTTOM)),
                   '3': list(chain(TOP, TOP_RIGHT, MIDDLE, BOTTOM_RIGHT, BOTTOM)),
                   '4': list(chain(TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_RIGHT)),
                   '5': list(chain(TOP, TOP_LEFT, MIDDLE, BOTTOM_RIGHT, BOTTOM)),
                   '6': list(chain(TOP, TOP_LEFT, BOTTOM_LEFT, MIDDLE, BOTTOM_RIGHT, BOTTOM)),
                   '7': list(chain(TOP, TOP_RIGHT, BOTTOM_RIGHT)),
                   '8': list(chain(TOP, TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM)),
                   '9': list(chain(TOP, TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_RIGHT)),
                   '.': DOT,
                   'a': list(chain(TOP, TOP_LEFT, TOP_RIGHT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT)),
                   'b': list(chain(TOP_LEFT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM)),
                   'c': list(chain(TOP, TOP_LEFT, BOTTOM_LEFT, BOTTOM)),
                   'd': list(chain(TOP_RIGHT, MIDDLE, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM)),
                   'e': list(chain(TOP, TOP_LEFT, MIDDLE, BOTTOM_LEFT, BOTTOM)),
                   'f': list(chain(TOP, TOP_LEFT, MIDDLE, BOTTOM_LEFT)),
                   ' ': []}

class PrintNeoPixel:
    def __init__(self, num_neopixels):
        self.neo_values = [(0, 0, 0)] * num_neopixels
        self.neo_length = num_neopixels

    def __setitem__(self, idx, colour):
        self.neo_values[idx] = colour

    def fill(self, colour):
        self.neo_values = [colour for _ in self.neo_values]

    def write(self):
        print(self.neo_values)

class Neo7Segment:

    def __init__(self, neopixel, num_chars):
        self.neopixel = neopixel
        self.num_chars = num_chars

    def display(self, display_string, colour):
        ''' Simple interface, single colour only '''
        assert len(display_string) <= self.num_chars

        self.neopixel.fill((0,0,0))
        for index, c in enumerate(display_string):
            for neo_index in char_to_segment[c.lower()]:
                self.neopixel[neo_index + (29 * index)] = colour
        self.neopixel.write()
