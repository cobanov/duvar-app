import psycopg2
import os


class DuvarovDB():
    def __init__(self) -> None:
        self._database = "d5ggjt80j3jic5"
        self._user = "lewormdmwvpmrv"
        self._host = "ec2-18-214-211-47.compute-1.amazonaws.com"

    def connect_db(self, password):
        self.connection = psycopg2.connect(database=self._database, user=self._user,
                                           password=password, host=self._host, port="5432")

    def get_data(self,  query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        self.connection.close()
        return data


mert = DuvarovDB()
mert.connect_db(os.getenv('db_password'))
query = """SELECT * FROM duvarapp LIMIT 10"""

data = mert.get_data(query)

for datum in data:
    print(datum)
