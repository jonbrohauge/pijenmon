"""
Class Consul Utilities

Manage communication with consul

"""
import socket

try:
    from consul import Consul
except ImportError:
    print("Consul was not found")


class ConsulUtilities:
    """Class containing supporting methods"""
    def __init__(self, consul=None, hostname=None, jenkins=None):
        self._consul = consul or Consul()
        if hostname is None:
            self.set_hostname()
        else:
            self.hostname = hostname
        if jenkins is None:
            jenkins = 'localhost'
        self.configuration = {'hostname': hostname, 'jenkins_url': jenkins}

    def set_hostname(self, hostname=None):
        """Set the hostname"""
        if hostname is None:
            hostname = socket.gethostname()  # pragma: no cover
        self.hostname = hostname.lower()

    def get_hostname(self):
        """Get the hostname"""
        return self.hostname
