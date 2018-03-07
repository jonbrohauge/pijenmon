"""
Class utilities

How to get jobs from a Jenkins-ci instance and query the builds for status
Inspired by: https://github.com/pycontribs/jenkinsapi/blob/master/examples/how_to/query_a_build.py

"""
try:
    from jenkinsapi.jenkins import Jenkins
except ImportError:
    print("Jenkins was not found")

try:
    from blinkt import Blinkt
except ImportError:
    print("Blinkt was not found")


class Utilities(object):
    """Class containing supporting methods"""

    def __init__(self, blinkt=None, jenkins=None):
        self._blinkt = blinkt or Blinkt()
        self._jenkins = jenkins or Jenkins()

    @staticmethod
    def set_color(status):
        """Translates Jenkins status to RGY"""
        return_value = 'Y'
        if status == 'success':
            return_value = 'G'
        elif status == 'failed':
            return_value = 'R'
        return return_value

    def set_pixel_bar(self, pixel_list):
        """Sets the proper color in the array used in priming the blinkt"""
        for x in range(len(pixel_list)):
            if pixel_list[x] == 'G':
                self.set_green(x)
            if pixel_list[x] == 'R':
                self.set_red(x)
            elif pixel_list[x] == 'Y':
                self.set_yellow(x)

    def set_green(self, pixel):
        """Sets the green color"""
        self._blinkt.set_pixel(pixel, 0, 255, 0)

    def set_red(self, pixel):
        """Sets the red color"""
        self._blinkt.set_pixel(pixel, 255, 0, 0)

    def set_yellow(self, pixel):
        """Sets the yellow color"""
        self._blinkt.set_pixel(pixel, 255, 255, 0)

    def get_jenkins_jobs_status(self):
        """Gets the status of all Jenkins Jobs"""
        status_list = []
        for key in self._jenkins.keys():
            if key.find('sample-applications') != -1:
                status_list.append(self.get_job_build_status(key))
        return status_list

    @staticmethod
    def get_job_build_status(self, jenkins_job_key):
        """Gets the build status of a specific Jenkins job"""
        job = self._jenkins.get_job(jenkins_job_key)
        last_build_number = job.get_last_buildnumber()
        gb = job.get_build(last_build_number)
        return gb.get_status()
