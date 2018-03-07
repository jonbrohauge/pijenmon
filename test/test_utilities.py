"""Tests the utilities"""

import unittest

try:
    from jenkinsapi.jenkins import Jenkins
except ImportError:
    print("Jenkins was not found")

try:
    from blinkt import Blinkt
except ImportError:
    print("Blinkt was not found")

from dk.legevognen.pijenmon.utilities import Utilities


class TestUtilities(unittest.TestCase):
    """This class contains tests related to the Utilities class"""

    def test_set_color(self):
        util = Utilities(TestBlinkt, TestJenkins)
        self.assertEqual('G', util.set_color('success'))
        self.assertEqual('R', util.set_color('failed'))
        self.assertEqual('Y', util.set_color('anything else'))

    def test_set_pixel_bar(self):
        util = Utilities(TestBlinkt, TestJenkins)
        test_list = ['R', 'G', 'Y']
        self.assertIsNone(util.set_pixel_bar(test_list))

    def test_jenkins_jobs_status(self):
        pass


class TestBlinkt:

    @staticmethod
    def set_pixel(place=None, red=None, green=None, blue=None):
        return True


class TestJenkins:

    @staticmethod
    def get_job(key=None):
        return '{"last_build_number": 1}'

    @staticmethod
    def keys():
        return '{}'
