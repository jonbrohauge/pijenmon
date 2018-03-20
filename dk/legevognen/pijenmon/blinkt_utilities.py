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
        self.blinkt_array = []
        for index in range(0, self._blinkt.NUM_PIXELS):
            self.blinkt_array.append('R')

    def set_green(self, pixel):
        """Sets the green color"""
        self._blinkt.set_pixel(pixel, 0, 255, 0)

    def set_red(self, pixel):
        """Sets the red color"""
        self._blinkt.set_pixel(pixel, 255, 0, 0)

    def set_yellow(self, pixel):
        """Sets the yellow color"""
        self._blinkt.set_pixel(pixel, 255, 255, 0)

    def set_black(self, pixel):
        """Sets the yellow color"""
        self._blinkt.set_pixel(pixel, 0, 0, 0)

    def show(self, job_status):
        number_of_green = int(job_status.count('SUCCESS')/len(job_status))
        number_of_red = int(job_status.count('FAILURE')/len(job_status))
        number_of_yellow = self._blinkt.NUM_PIXELS - (number_of_green + number_of_red)
        if number_of_yellow < 0:
            number_of_yellow = 0

        self._blinkt.clear()

        for pixel_count in range(0, self._blinkt.NUM_PIXELS):
            if number_of_green > 0:
                self.set_green(pixel_count)
                number_of_green -= 1
            elif number_of_red > 0:
                self.set_red(pixel_count)
                number_of_red -= 1
            elif number_of_yellow > 0:
                self.set_yellow(pixel_count)
                number_of_yellow -= 1
            else:
                self.set_black(pixel_count)

        self._blinkt.show()
