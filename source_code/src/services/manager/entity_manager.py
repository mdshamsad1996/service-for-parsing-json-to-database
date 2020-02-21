"""
Interface defination for a generic entity manager
"""

from abc import abstractmethod, ABC


class IEntityManager(ABC):
    """
    Defines an interface for an abstract entity manager
    """

    def __init__(self, name, data_store):
        self.name = name
        self.data_store = data_store

    @abstractmethod
    def fetchall(self) -> int:
        """
        Abstract method to fetch records
        """

    @abstractmethod
    def add_record(self, entity) -> None:
        """
        Abstract method for adding record
        """
