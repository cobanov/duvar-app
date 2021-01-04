import psycopg2
import os
from app.entryController import entryContentCheck, entryFilter


## Credentials
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


# Queries
CREATE_ENTRY = "INSERT INTO public.duvarapp (content_msg) VALUES (%s)"
RETRIEVE_ENTRIES = "SELECT * FROM public.duvarapp ORDER BY message_id ASC"
RETRIEVE_ENTRIES_TOP = "SELECT * FROM public.duvarapp ORDER BY vote_count ASC"
UPVOTE = "UPDATE public.duvarapp SET vote_count = vote_count + 1 WHERE message_id = (%s)"
DELETE_ENTRY = "DELETE FROM public.duvarapp WHERE message_id = (%s)"
WIPE = "DELETE FROM public.duvarapp WHERE message_id < (%s)"


# conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
#                         password=DB_PASSWORD, host=DB_HOST)

def create_entry(content):
    if entryContentCheck(content):
        content = entryFilter(content)
        with psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as connection:
            cursor = connection.cursor()
            cursor.execute(CREATE_ENTRY, (content,))
            connection.commit()

def retrieve_entries():
    with psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES)
        return cursor.fetchall()

def retrieve_entries_top():
    with psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIES_TOP)
        return cursor.fetchall()

def upvote(message_id):
    with psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as connection:
        cursor = connection.cursor()
        cursor.execute(UPVOTE, (message_id, ))
        connection.commit()


def delete(message_id):
    with psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_ENTRY, (message_id, ))
        connection.commit()


def wipe(message_id):
    with psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as connection:
        cursor = connection.cursor()
        cursor.execute(WIPE, (message_id, ))
        connection.commit()

