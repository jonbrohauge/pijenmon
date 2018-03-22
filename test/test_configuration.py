"""Tests the code related to the configuration of the application"""
import unittest
from dk.legevognen.pijenmon.configuration import Configuration


class TestConfiguration(unittest.TestCase):
    """Performs unit tests on the class JenkinsInteraction"""

    def setUp(self):
        """Setup the test class"""
        self.hostname = 'testhost'
        self.configuration = Configuration(self.hostname, 'http://testhost/jenkins')
        self.test_dictionary = {'hostname': self.hostname, 'jenkins_url': 'http://testhost/jenkins'}

    def test_get_hostname(self):
        """Test for setting the hostname correctly"""
        self.assertEqual(self.hostname, self.configuration.get_hostname())

    def test_get_configuration(self):
        """Test retrieving the configuration object"""
        self.assertDictEqual(self.test_dictionary, self.configuration.get_configuration())
