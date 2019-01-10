"""Contains application configuration"""
import consul
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

    def init_configuration(self, keyvalue_connection):
        client = consul.Consul(host=keyvalue_connection[0])
        # client = etcd3.client(keyvalue_connection[0], keyvalue_connection[1])
        for value, meta in client.get_prefix('/' + self.get_hostname()):
            key = re.split(r'/', meta.key.decode("utf-8"))
            self.configuration[key[2]] = value.decode("utf-8")

    def set_configuration(self, keyvalue_connection, property_dictionary):
        """Set the configuration"""
        client = consul.Consul(host=keyvalue_connection[0])
        # client = etcd3.client(keyvalue_connection[0], keyvalue_connection[1])
        dictionary_keys = property_dictionary.keys()
        for key in dictionary_keys:
            client_key = '/' + self.get_hostname() + '/' + key
            client.put(client_key, property_dictionary[key])

    def get_configuration(self):
        """Get the configuration for the application"""
        return self.configuration

    def set_configuration_property(self, keyvalue_connection, key, value):
        """Add a configuration key value pair"""
        self.set_configuration(keyvalue_connection, {key: value})

    def set_hostname(self, hostname=None):
        """Set the hostname"""
        if hostname is None:
            hostname = socket.gethostname()  # pragma: no cover
        self.hostname = hostname.lower()

    def get_hostname(self):
        """Get the hostname"""
        return self.hostname
