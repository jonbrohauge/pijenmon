"""Contains application configuration"""
import etcd3
import socket
import re


class Configuration:
    """This class contains application configuration"""

    def __init__(self, hostname=None, jenkins=None):
        if hostname is None:
            self.set_hostname()
        else:
            self.hostname = hostname
        if jenkins is None:
            jenkins = 'localhost'
        self.configuration = {'hostname': hostname, 'jenkins_url': jenkins}

    def init_configuration(self, etcd_connection):
        client = etcd3.client(etcd_connection[0], etcd_connection[1])
        for value, meta in client.get_prefix('/' + self.get_hostname()):
            key = re.split(r'/', meta.key.decode("utf-8"))
            self.configuration[key[2]] = value.decode("utf-8")

    def set_configuration(self, etcd_connection, property_dictionary):
        """Set the configuration"""
        client = etcd3.client(etcd_connection[0], etcd_connection[1])
        dictionary_keys = property_dictionary.keys()
        for key in dictionary_keys:
            client_key = '/' + self.get_hostname() + '/' + key
            client.put(client_key, property_dictionary[key])

    def get_configuration(self):
        """Get the configuration for the application"""
        return self.configuration

    def set_configuration_property(self, etcd_connection, key, value):
        """Add a configuration key value pair"""
        self.set_configuration(etcd_connection, {key: value})

    def set_hostname(self, hostname=None):
        """Set the hostname"""
        if hostname is None:
            hostname = socket.gethostname()  # pragma: no cover
        self.hostname = hostname.lower()

    def get_hostname(self):
        """Get the hostname"""
        return self.hostname
