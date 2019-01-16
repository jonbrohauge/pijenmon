"""
This script is not really meant to run.
It is more meant as a way for me to dump my brain into python'ish
"""


def get_configuration_from_kv_store(hostname):
    """
    Retrieve the configuration from the key/value-store.
    If there is no configuration for the specific host, create a new entry based on default values.

    Return value should be a dict of the configuration.
    """
    print("Get configuration from key/value-store where hostname: " + hostname)
    configuration_entry_does_not_exist = True
    if configuration_entry_does_not_exist:
        print("Create configuration entry in key/value-store where hostname: " + hostname)
    return []


def get_jenkins_job_status(jenkins_url):
    """
    Retrieve the build status of all jobs from a specific Jenkins instance.

    Return value should be a list of job results. Where the status is not one of: SUCCESS, UNSTABLE, and FAILURE,
    the value should count as UNSTABLE.
    """
    print("Get build status from all jobs from this Jenkins instance: " + jenkins_url)
    return []


def parse_job_results(job_results):
    """
    Parse the list of job statuses, and concatenate the list into a result set of three possible values,
    containing the keys: success, unstable, and failure, where their values reflect the corresponding number of jobs
    with that exact status.

    Return value should be a dict of the three elements (success, unstable, and failure), each with a numerical value.
    """
    print("Get the status from each job, and match it against SUCCESS, UNSTABLE, and FAILURE")
    return []


def update_blinkt_panel(results):
    """
    Parse the results, and set the correct amount of pixels (LEDs) with a specific color, based on the result, where:
    SUCCESS gives a green light
    UNSTABLE gives a yellow light
    FAILURE gives a red light
    """
    print("Colorize each of the 8 LEDs correctly based on the input")


def start():
    configuration_object = get_configuration_from_kv_store("hostname")
    jenkins_job_results = get_jenkins_job_status(configuration_object['Jenkins_URL'])
    blinkt_panel_input = parse_job_results(jenkins_job_results)
    update_blinkt_panel(blinkt_panel_input)


if __name__ == "__main__":
    start()
