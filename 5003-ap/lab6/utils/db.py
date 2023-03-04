import atexit
from time import sleep
from mysql.connector import connect
from dotenv import load_dotenv
from pathlib import Path
import os


class db:
    def __init__(self) -> None:
        # load the .env file
        path = Path(__file__).parent.parent
        load_dotenv(dotenv_path=f"{path}/.env")
        self.connect()
        atexit.register(self.disconnect)

    def connect(self) -> None:
        try:
            self.mydb = connect(
                host="127.0.0.1",
                user="root",
                password=os.environ.get("MYSQL_PASSWORD"),
            )
            self.cursor = self.mydb.cursor(buffered=True)
            self.cursor.execute("USE ap5003")
        except Exception as e:
            print("\tError connecting to the database", "\n\tRetrying in 2 seconds...")
            if "HY000" in str(e):
                sleep(2)
                self.connect()

    def disconnect(self) -> None:
        print("\n\n\n")
        try:
            self.cursor.close()
            self.mydb.close()
            self.mydb.disconnect()
        except Exception as _e:
            pass

    def get(
        self,
        table: str = None,
        field: str = "*",
        where: str = None,
        sort: str = None,
        raw_query: str = None,
    ):
        if raw_query is not None:
            query = raw_query
        else:
            query = f"SELECT {field} FROM {table}"
            if where is not None:
                query += f" WHERE {where}"
            if sort is not None:
                query += f" ORDER BY {sort}"
        data = None
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
        except Exception as e:
            # print("\n\t" + str(e))
            return None
        return data

    def set(self, table: str, keys: str, values: str):
        self.cursor.execute(f"INSERT INTO {table} ({keys}) VALUES ({values})")
        data = self.mydb.commit()
        return True

    def delete(self, key: str):
        self.cursor.execute(f"DELETE FROM {key}")
        data = self.cursor.fetchall()
        return data

    def raw(self, queries: str):
        queries = queries.split(";")
        for query in queries:
            if query.strip() == "":
                continue
            self.cursor.execute(query)
            self.mydb.commit()
