import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT,
                                email TEXT,
                                password TEXT,
                                register_date TEXT                                
                            )
                            ''')
        self.connection.commit()

    def read_data(self):
        self.cursor.execute("SELECT * FROM accounts")
        data = self.cursor.fetchall()
        return data

    def insert_data(self, username, email, password, register_date):
        self.cursor.execute("INSERT INTO accounts (username, email, password, register_date) VALUES (?, ?, ?, ?)", (username, email, password, register_date))
        self.connection.commit()

if __name__ == "__main__":
    db = Database("db.sqlite3")

