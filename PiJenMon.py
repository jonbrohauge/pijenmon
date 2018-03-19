import os
import time
from jenkinsapi.jenkins import Jenkins
from blinkt import Blinkt
from dk.legevognen.pijenmon.configuration import Configuration
from dk.legevognen.pijenmon.jenkins_utilities import JenkinsUtilities
from dk.legevognen.pijenmon.blinkt_utilities import BlinktUtilities


def pijenmon():

    config = Configuration(None)
    run_once = True
    etcd_hostname = "localhost"
    etcd_port = 2379
    etcd_configuration = (etcd_hostname, etcd_port)
    config.init_configuration(etcd_configuration)

    def clear_shell():
        os.system('cls' if os.name == 'nt' else 'clear')

    def check_jenkins(jenkins_url):
        jenkins_utility = JenkinsUtilities(Jenkins(jenkins_url))
        status_count = {'total': 0, 'success_count': 0, 'failure_count': 0, 'else_count': 0}
        for job_status in jenkins_utility.get_jenkins_jobs_status():
            if job_status == 'SUCCESS':
                status_count['success_count'] += 1
            elif job_status == 'FAILURE':
                status_count['failure_count'] += 1
            else:
                status_count['else_count'] += 1
            status_count['total'] += 1
        return status_count

    # Add a value to the current property dictionary
    # config.set_configuration_property(etcd_configuration, 'testkey2', 'testvalue2')

    def run_blinkt(job_status):
        number_of_pixels = 8
        blinkt_utility = BlinktUtilities(Blinkt)
        # print('Total: ', job_status['total'])
        # print('Number of successes: ', job_status['success_count'])
        # print('Number of failures: ', job_status['failure_count'])
        # print('Number of else: ', job_status['else_count'])
        jobs_per_pixel = job_status['total'] / number_of_pixels
        number_of_green = int((job_status['success_count'] / job_status['total']) * number_of_pixels)
        number_of_yellow = int((job_status['else_count'] / job_status['total']) * number_of_pixels)
        number_of_red = int((job_status['failure_count'] / job_status['total']) * number_of_pixels)
        number_of_black = number_of_pixels - (number_of_green + number_of_yellow + number_of_red)
        print('Number of jobs per pixel: ', jobs_per_pixel)
        print('Number of green pixels: ', number_of_green, 'Number of yellow pixels: ', number_of_yellow,
              'Number of red pixels: ', number_of_red)
        if number_of_black > 0:
            print('Number of black pixels: ', number_of_black)
        while (number_of_pixels > 0) and (number_of_green > 0):
            blinkt_utility.set_green(number_of_pixels)
            number_of_green -= 1
            number_of_pixels -= 1
        while (number_of_pixels > 0) and (number_of_yellow > 0):
            blinkt_utility.set_yellow(number_of_pixels)
            number_of_green -= 1
            number_of_pixels -= 1
        while (number_of_pixels > 0) and (number_of_red > 0):
            blinkt_utility.set_red(number_of_pixels)
            number_of_green -= 1
            number_of_pixels -= 1

    while True:
        if config.configuration['jenkins_url'] is not None:
            print('Looking at Jenkins', config.configuration['jenkins_url'])
            status = check_jenkins(config.configuration['jenkins_url'])
            run_blinkt(status)

        else:
            raise LookupError('URL to Jenkins not found')

        time.sleep(5)
        if run_once:
            break


if __name__ == "__main__":
    pijenmon()
