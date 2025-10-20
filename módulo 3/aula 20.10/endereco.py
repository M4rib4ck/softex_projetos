import sqlite3
from database import DatabaseConnection

class endereços:
    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn
        self._create_table()
    def _create_table(self):
            self.db_conn.connect()
            self.db_conn.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS endereços (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    endereço TEXT NOT NULL
                );
            """
            )
            self.db_conn.close()
