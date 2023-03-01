from mysql.connector import connect
from dotenv import load_dotenv
from pathlib import Path
import os


class db:
    def __init__(self) -> None:
        # load the .env file
        path = Path(__file__).parent.parent
        load_dotenv(dotenv_path=f"{path}/.env")

    def connect(self) -> None:
        try:
            self.mydb = connect(
                host="127.0.0.1", user="root", password=os.environ.get("MYSQL_PASSWORD")
            )
            self.cursor = self.mydb.cursor()
        except Exception as e:
            print(e)
            self.cursor = None

    def disconnect(self) -> None:
        self.mydb.close()

    def get(
        self,
        table: str,
        field: str = "*",
        where: str = None,
        sort: str = None,
        raw_query: str = None,
    ) -> str:
        if raw_query is not None:
            query = raw_query
        else:
            query = f"SELECT {field} FROM {table}"
            if where is not None:
                query += f" WHERE {where}"
            if sort is not None:
                query += f" ORDER BY {sort}"
        data = self.cursor.execute(query)
        return data

    def set(self, key: str, value: str):
        data = self.cursor.execute(f"INSERT INTO {key} VALUES ({value})")
        return data

    def delete(self, key: str):
        data = self.cursor.execute(f"DELETE FROM {key}")
        return data

    def raw(self, query: str):
        data = self.cursor.execute(query)
        return data
