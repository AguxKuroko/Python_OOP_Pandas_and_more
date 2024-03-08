import pandas as pd
from sqlalchemy import create_engine
import maskpass as ms
import numpy as np


class ConnectionToDatabase:
    objects_in_class = []

    def __init__(self):
        self.engine = self.init_engine()
        self.name = input("Name created object: ")
        self.objects_in_class.append(self)

    @staticmethod
    def credentials():
        """Gets credentials necessary for database connection."""
        print()
        data = ms.askpass(
            "Insert necessary information in order to connect to database:\nuser,password,hostname,port and database:\n")
        username, password, hostname, port, database = data.lower().split(",")
        return username, password, hostname, port, database

    def connect_to_database(self):
        """Connects the user to a database."""
        username, password, hostname, port, database = self.credentials()
        mydb_connection = f'mysql+pymysql://{username}:{password}@{hostname}:{int(port)}/{database}'
        return mydb_connection

    def init_engine(self):
        """Creates an engine to retrieve data from a database."""
        engine = create_engine(self.connect_to_database())
        return engine

    def close_engine(self):
        """Closes the engine after extracting data."""
        self.engine.dispose()

    def __repr__(self):
        print(f"{self.__class__.__name__} >>>> object name '{self.name}'")
        return f"The number of objects = {str(len(self.objects_in_class))}"


class GettingDataFromDatabase(ConnectionToDatabase):
    objects_in_class = []

    def __init__(self):
        super().__init__()
        self.objects_in_class.pop()

        GettingDataFromDatabase.objects_in_class.append(self)

    def get_data(self):
        """Getting data from a database using SQL statement."""
        print()
        query = input("Please provide an SQL query that you wish to execute ↓\n")
        if not query.startswith('select'):
            raise SelectError("Inserted text doesn't start with 'SELECT'")
        print()

        data = pd.read_sql(query, con=self.engine)
        self.close_engine()
        return data


class SelectError(ValueError):
    def __init__(self, message):
        super().__init__(message)
