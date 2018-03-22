import os
import time
from jenkinsapi.jenkins import Jenkins
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
    blinkt_utility = BlinktUtilities()

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

    while True:
        if config.configuration['jenkins_url'] is not None:
            print('Looking at Jenkins', config.configuration['jenkins_url'])
            jenkins_utility = JenkinsUtilities(config.configuration['jenkins_url'])
            blinkt_utility.show(jenkins_utility.get_jenkins_jobs_status())

        else:
            raise LookupError('URL to Jenkins not found')

        time.sleep(5)
        if run_once:
            break


if __name__ == "__main__":
    pijenmon()
