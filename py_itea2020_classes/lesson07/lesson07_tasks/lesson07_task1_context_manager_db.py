import sqlite3


class MyDBConnection:

    def __init__(self, file_name):
        self._connect = sqlite3.connect(file_name)
        self._cursor = self._connect.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()


with MyDBConnection('my_sqlite_database.db') as c:
    c._cursor.execute('select * from parking')
    print(c._cursor.fetchone())