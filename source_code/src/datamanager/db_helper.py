"""
Database helper to read/write from/to MySql databases
"""


class DBHelper():
    """
    Helper to interact with Database
    """

    def __init__(self, connection):
        """
        Initialized connection with specified data base
        """
        self.db_connection = connection
        self.db_cursor = self.db_connection.cursor()

    def insert(self, table, fields, values) ->None:
        """
        Inserts data into table as specified by the lists: fields and values
        """

        query = ''

        query = "insert into {} ({}) values ({})".format(table,\
                    self.to_attribute_list_str(fields, ""),\
                    self.to_attribute_list_str(values, "'"))

        self.db_cursor.execute(query)
        self.db_connection.commit()

    def fetch(self, table) -> int:
        """
        fetches number of records inserted
        """

        query = ''

        query = 'select COUNT(*) from {}'.format(table)

        self.db_cursor.execute(query)

        no_of_records = self.db_cursor.fetchall()[0]

        return no_of_records

    def to_attribute_list_str(self, attribute_list, separator) -> str:
        """
        conver a list of attributes to a comma  separated string of attributes
        """

        attribute_list_str = ''
        for attribute in attribute_list[0:-1]:
            attribute_list_str += '{}{}{},'.format(separator, attribute, separator)

        attribute_list_str += '{}{}{}'.format(separator, str(attribute_list[-1]), separator)

        return attribute_list_str
