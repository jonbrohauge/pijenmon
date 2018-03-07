"""
Class utilities

How to get jobs from a Jenkins-ci instance and query the builds for status
Inspired by: https://github.com/pycontribs/jenkinsapi/blob/master/examples/how_to/query_a_build.py
"""

try:
    from jenkinsapi.jenkins import Jenkins
except ImportError:
    print("Jenkins was not found")


class Utilities(object):
    """Class containing supporting methods"""

    def __init__(self, jenkins=None):
        self._jenkins = jenkins or Jenkins()

    @staticmethod
    def get_job_build_status(self, jenkins_job_key):
        """Gets the build status of a specifik Jenkins job"""
        job = self._jenkins.get_job(jenkins_job_key)
        last_build_number = job.get_last_buildnumber()
        gb = job.get_build(last_build_number)
        return gb.get_status()