"""Contains application configuration"""
import json
import socket


class Configuration:
    """This class contains application configuration"""

    def __init__(self, hostname=None, jenkins=None, github=None):
        self.hostname = hostname
        self.jenkins_url = jenkins
        self.github_url = github

    def set_configuration(self, configuration_json):
        """Set initial configuration"""
        configuration = json.loads(configuration_json)
        self.set_hostname(configuration['hostname'])
        self.set_jenkins_url(configuration['jenkins_url'])
        self.set_github_url(configuration['github_url'])

    def get_configuration(self):
        """Get the configuration for the application"""
        return json.dumps(self.__dict__, sort_keys=True)

    def set_github_url(self, url):
        """Set GitHub URL"""
        self.github_url = url

    def get_github_url(self):
        """Get GitHub URL"""
        return self.github_url

    def set_jenkins_url(self, url):
        """Set Jenkins URL"""
        self.jenkins_url = url

    def get_jenkins_url(self):
        """Get Jenkins URL"""
        return self.jenkins_url

    def set_hostname(self, hostname=None):
        """Set the hostname"""
        if hostname is None:
            hostname = socket.gethostname()  # pragma: no cover
        self.hostname = hostname

    def get_hostname(self):
        """Get the hostname"""
        return self.hostname
