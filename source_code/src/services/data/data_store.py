"""
Interface defination for a generic object data store
"""
from abc import abstractmethod, ABC


class IDataStore(ABC):
    """
    Defines an interface for an abstract object data store
    """

    @abstractmethod
    def read(self, path):
        """
        Abstract method for reading an object
        """
    @abstractmethod
    def write(self, path, value):
        """
        Abstract method for writing an object
        """
