"""
Implementation of IDataStore Service with MySql as the data store
"""

from src.services.data.data_store import IDataStore


class DBDatastore(IDataStore):
    """
    Use this class to manage object with a MySQl data base
    """

    def __init__(self, db_helper):
        """
        Constructor
        """
        self.db_helper = db_helper

    def read(self, path) -> None:
        """
        Read an object identified by path
        """
        return self.db_helper.fetch(path)

    def write(self, path, value) -> None:
        """
        write an object identified by a path to the database
        """
        table = path[0]      # argument 1 is the table name
        start_index = 1
        fields = path[start_index:]
        values = value

        self.db_helper.insert(table, fields, values)
