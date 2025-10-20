import sqlite3


class DatabaseConnection:
    def __init__(self, db_name="escola.db"):
        self.db_name = db_name
        self.conn = None 
        self.cursor = None

    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cursor = None



if __name__ == "__main__":
    db = DatabaseConnection()
    db.connect()
    print("Conexão com o banco de dados estabelecida.")
    db.close()
    print("Conexão com o banco de dados encerrada.")
