import sqlite3
from app.entryController import entryContentCheck, entryFilter

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries (message_id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL UNIQUE, date TEXT, vote INTEGER)"
CREATE_ENTRY = "INSERT INTO entries VALUES (?, ?, ?, ?)"
RETRIEVE_ENTRIES = "SELECT * FROM entries"
RETRIEVE_ENTRIES_TOP = "SELECT * FROM entries ORDER BY vote ASC"
WIPE_ENTRIES = "DROP TABLE entries"
UPVOTE = "UPDATE entries SET vote = vote + 1 WHERE message_id = (?)"
DELETE_ENTRY = "DELETE FROM entries WHERE message_id = (?)"

message_id = 1


def create_tables():
    with sqlite3.connect("data.db") as connection:
        connection.execute(CREATE_TABLE)


def create_entry(content, date):

    global message_id

    if entryContentCheck(content):
        content = entryFilter(content)
        with sqlite3.connect("data.db") as connection:

            try:
                connection.execute(
                    CREATE_ENTRY, (message_id, content, date, 0))
                message_id += 1

            except Exception as e:
                if "message_id" in str(e):
                    while True:
                        try:
                            connection.execute(
                                CREATE_ENTRY, (message_id, content, date, 0))
                            message_id += 1
                            break

                        except:
                            message_id += 1


def retrieve_entries():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES)
        return cursor.fetchall()


def retrieve_entries_top():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES_TOP)
        return cursor.fetchall()


def upvote(message_id):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(UPVOTE, (message_id, ))


def delete(message_id):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_ENTRY, (message_id, ))


def clear_database():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(WIPE_ENTRIES)
        connection.execute(CREATE_TABLE)
