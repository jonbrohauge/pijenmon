"""
Class Blinkt Utilities

How to show a row of LED in different colors on a Pimoroni Blinkt
Inspired by: http://docs.pimoroni.com/blinkt/

"""
try:
    from blinkt import Blinkt
except ImportError:
    print("Blinkt was not found")


class BlinktUtilities:
    """Class containing supporting methods"""
    def __init__(self, blinkt=None):
        self._blinkt = blinkt or Blinkt()

    def set_green(self, pixel):
        """Sets the green color"""
        self._blinkt.set_pixel(pixel, 0, 255, 0)

    def set_red(self, pixel):
        """Sets the red color"""
        self._blinkt.set_pixel(pixel, 255, 0, 0)

    def set_yellow(self, pixel):
        """Sets the yellow color"""
        self._blinkt.set_pixel(pixel, 255, 255, 0)