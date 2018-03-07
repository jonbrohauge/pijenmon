"""Tests the code related to the configuration of the application"""
import unittest
from dk.legevognen.pijenmon.configuration import Configuration


class TestConfiguration(unittest.TestCase):
    """Performs unit tests on the class JenkinsInteraction"""

    def setUp(self):
        """Setup the test class"""
        self.configuration_json = '{"hostname": "localhost", \
                                "jenkins_url": "http://jenkinspi:8080/jenkins", \
                                "github_url": "http://github.com/jonbrohauge"}'
        self.configuration = Configuration()

    def test_set_github_url(self):
        """Test for setting GitHub URL correctly"""
        self.configuration.set_configuration(
            self.configuration_json)
        self.assertEqual("http://github.com/jonbrohauge",
                         self.configuration.get_github_url())
        self.assertNotEqual("http://github.com/",
                            self.configuration.get_github_url())

    def test_set_jenkins_url(self):
        """Test for setting Jenkins URL correctly"""
        self.configuration.set_configuration(
            self.configuration_json)
        self.assertEqual("http://jenkinspi:8080/jenkins",
                         self.configuration.get_jenkins_url())
        self.assertNotEqual("http://localhost:8080/",
                            self.configuration.get_jenkins_url())

    def test_get_hostname(self):
        """Test for setting the hostname correctly"""
        hostname = 'localhost'
        self.configuration.set_hostname(hostname)
        self.assertEqual(hostname, self.configuration.get_hostname())

    def test_get_configuration(self):
        """Test retrieving the configuration object"""
        json_test_input = '{"github_url": "http://github.com/jonbrohauge", "hostname": "localhost", "jenkins_url": "http://jenkinspi:8080/jenkins"}'
        self.configuration.set_configuration(json_test_input)
        self.assertEqual(json_test_input, self.configuration.get_configuration())
