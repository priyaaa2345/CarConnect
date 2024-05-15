class DatabaseConnectionException(Exception):
    def __init__(self):
        super().__init__("Unable to establish a connection to database")