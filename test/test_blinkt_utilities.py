"""Tests the utilities"""

import unittest

try:
    from blinkt import Blinkt
except ImportError:
    print("Blinkt was not found")

from dk.legevognen.pijenmon.blinkt_utilities import BlinktUtilities


class TestUtilitiesBlinkt(unittest.TestCase):
    """This class contains tests related to the Utilities class"""

    def test_show(self):
        utilities = BlinktUtilities(TestBlinkt)
        utilities.show(['SUCCESS', 'FAILURE', 'SUCCESS'])


class TestBlinkt:
    NUM_PIXELS = 8

    @staticmethod
    def set_pixel(place=None, red=None, green=None, blue=None):
        return True

    @staticmethod
    def clear():
        pass

    @staticmethod
    def show():
        pass