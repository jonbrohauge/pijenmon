"""Tests the utilities"""

import unittest

try:
    from jenkinsapi.jenkins import Jenkins
except ImportError:
    raise ImportError("Jenkins was not found")

from dk.legevognen.pijenmon.jenkins_utilities import JenkinsUtilities


class TestUtilitiesJenkins(unittest.TestCase):
    """This class contains tests related to the Utilities class"""

    def test_jenkins_jobs_status(self):
        utilities = JenkinsUtilities(TestJenkins)
        self.assertEqual(utilities.get_jenkins_jobs_status(), ['SUCCESS'])
        self.assertNotEqual(utilities.get_jenkins_jobs_status(), ['FAILURE'])


class TestJenkins:

    @staticmethod
    def get_job(key=None):
        return TestJenkinsJob

    @staticmethod
    def keys():
        return ['TestBuild']


class TestJenkinsJob:

    @staticmethod
    def __init__(self):
        self.name = 'TestJobName'
        self.build_number = 1

    @staticmethod
    def get_last_buildnumber():
        return 1

    @staticmethod
    def get_build(build_number=None):
        return TestJenkinsBuild


class TestJenkinsBuild:

    @staticmethod
    def get_status():
        return 'SUCCESS'
