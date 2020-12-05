import sqlite3

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries (content TEXT NOT NULL UNIQUE, date TEXT)"
CREATE_ENTRY = "INSERT INTO entries VALUES (?, ?)"
RETRIEVE_ENTRIES = "SELECT * FROM entries ORDER BY date ASC"
WIPE_ENTRIES = "DROP TABLE entries"

def create_tables():
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_TABLE)


def create_entry(content, date):
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_ENTRY, (content, date))


def retrieve_entries():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES)
        return cursor.fetchall()

def clear_database():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(WIPE_ENTRIES)
        connection.execute(CREATE_TABLE)