"""
Class Consul Utilities

Manage communication with consul

"""
try:
    from consul import Consul
except ImportError:
    print("Consul was not found")


class ConsulUtilities:
    """Class containing supporting methods"""
    def __init__(self, consul=None):
        self._consul = consul or Consul()
