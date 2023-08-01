import sqlite3
from typing import Tuple, Any

from tgbot.models.Enums import University


class Database:
    def __init__(self, path: str):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        self.table_name = "users"

    def user_exists(self, user_id: int):
        self.cursor.execute(f"SELECT DISTINCT * FROM {self.table_name} "
                            f"WHERE user_id=?", (user_id,))

        data = self.cursor.fetchone()
        return bool(data)

    def get_user(self, user_id: int) -> Tuple[Any]:
        self.cursor.execute(f"SELECT DISTINCT * FROM {self.table_name} "
                            f"WHERE user_id=?", (user_id,))

        data = self.cursor.fetchone()
        return data

    def add_user(self, user_id: int, username: str, nickname: str, university: University) -> bool:
        if not self.user_exists(user_id):
            self.cursor.execute(f"INSERT INTO {self.table_name} (user_id, username, nickname, university) "
                                "VALUES (?, ?, ?, ?)", (user_id, username, nickname, university.value))
            self.connection.commit()
            return True

        raise Exception("User already exists")

    def print_all(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name};")
        for row in self.cursor.fetchall():
            print(row)

    def close_connection(self):
        """Close the connection"""
        self.connection.close()
