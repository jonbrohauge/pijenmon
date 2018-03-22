"""
Class Jenkins Utilities

How to get jobs from a Jenkins-ci instance and query the builds for status
Inspired by: https://github.com/pycontribs/jenkinsapi/blob/master/examples/how_to/query_a_build.py

"""
try:
    from jenkinsapi.jenkins import Jenkins
except ImportError:
    raise ImportError("Jenkins was not found")


class JenkinsUtilities:
    """Class containing supporting methods"""

    def __init__(self, jenkins=None):
        self._jenkins = jenkins or Jenkins()

    def get_jenkins_jobs_status(self):
        """Get the status of all Jenkins Jobs"""
        status_list = []
        for key in self._jenkins.keys():
            if key.find('sample-applications') == -1:
                status_list.append(self.get_job_build_status(key))
        return status_list

    def get_job_build_status(self, jenkins_job_key):
        """Get the build status of a specific Jenkins job"""
        job = self._jenkins.get_job(jenkins_job_key)
        last_build_number = job.get_last_buildnumber()
        gb = job.get_build(last_build_number)
        return gb.get_status()
