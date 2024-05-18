
class DatabaseContext:
    def __init__(self, db_name):
        self._db_name = db_name
        self._connection = None

    def connect(self):
        if self._connection is None:
            self._connection = sqlite3.connect(self._db_name)
        return self._connection

    def disconnect(self):
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def execute_query(self, query, params=None):
        if params is None:
            params = []
        cursor = self.connect().cursor()
        cursor.execute(query, params)
        self.connect().commit()
        return cursor

    def fetch_all(self, query, params=None):
        cursor = self.execute_query(query, params)
        return cursor.fetchall()

    def fetch_one(self, query, params=None):
        cursor = self.execute_query(query, params)
        return cursor.fetchone()
