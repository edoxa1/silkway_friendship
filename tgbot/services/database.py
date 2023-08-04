from datetime import datetime
from random import randint
import sqlite3

from tgbot.models import Enums
from tgbot.models import User
from tgbot.models import Profile


class Database:
    __instance = None

    @staticmethod
    def get_instance():
        if not Database.__instance:
            raise Exception("No instance")

        return Database.__instance

    def __init__(self, path: str, table_names: list[str]) -> None:
        """
        :param path: Path from CWD to database [.db]
        :param table_names: contains table names, len(table_names) = 3
        """
        if Database.__instance:
            raise Exception("Database instance already exists")

        self.users_table = UsersTable(path, table_names[0])
        self.profiles_table = ProfilesTable(path, table_names[1])
        self.universities_table = UniversitiesTable(path, table_names[2])

        Database.__instance = self
        # self.create_tables()

    def create_tables(self):
        self.users_table.create_table()
        self.profiles_table.create_table()
        self.universities_table.create_table()


class BaseTable:
    def __init__(self, path: str, table_name: str):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        self.table_name = table_name
        
    def print_all(self):
        print("-" * 10)
        print(f"DATA FOR {self.table_name}")
        self.cursor.execute(f"SELECT * FROM {self.table_name};")
        for row in self.cursor.fetchall():
            print(row)

    def get_count(self) -> int:
        print(f"GET COUNT FOR {self.table_name}")
        self.cursor.execute(f"SELECT COUNT(id) FROM {self.table_name};")
        return int(self.cursor.fetchone()[0])

    def close_connection(self):
        """Close the connection"""
        self.connection.close()

    def __del__(self):
        self.connection.commit()
    

class UsersTable(BaseTable):
    def __init__(self, path: str, table_name: str):
        super().__init__(path, table_name)
        
    def user_exists(self, user_id: int) -> bool:
        try:
            self.get_user(user_id)
            return True
        except:
            return False

    def get_user(self, user_id: int) -> User.User:
        self.cursor.execute(f"SELECT DISTINCT * FROM {self.table_name} "
                            f"WHERE user_id=?", (user_id, ))

        data = self.cursor.fetchone()
        if data:
            return User.User(user_id, Enums.University(data[2]), data[3], data[4], data[5])

        raise Exception("User not found")
    
    def add_user(self, user_id: int, university: Enums.University) -> User:
        """Add user if not exists. If exists, raises an error 'User already exists'
        :param user_id: user id
        :param university: University(Enum) -> NU = 1, AITU = 2

        :return: tgbot.models.User
        
        """
        if not self.user_exists(user_id):
            code = randint(10 ** 5, 10 ** 6 - 1)
            self.cursor.execute(f"INSERT INTO {self.table_name} "
                                f"(user_id, university, is_verified, is_banned, verification_code) "
                                "VALUES (?, ?, ?, ?, ?)", (user_id, university.value, False, False, code))
            self.connection.commit()
            return User.User(user_id, university, False, False, code)

        raise Exception("User already exists")
    
    def get_user_verification_code(self, user_id: int) -> int:
        self.cursor.execute(f"SELECT verification_code FROM {self.table_name} "
                            f"WHERE user_id=?", (user_id, ))
        data = self.cursor.fetchone()
        if data:
            return int(data[0])

        return None
    
    def create_table(self):
        self.cursor.execute(f"CREATE TABLE {self.table_name} ("
                            f"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            f"user_id INTEGER NOT NULL,"
                            f"university INTEGER,"
                            f"is_verified BOOL,"
                            f"is_banned BOOL,"
                            f"verification_code INTEGER);")
        
        self.connection.commit()
    

class ProfilesTable(BaseTable):
    def __init__(self, path: str, table_name: str):
        super().__init__(path, table_name)

    def add_profile(self, user_id: int, nickname: str, description: str, photo_id: str,
                    is_active: bool, create_date: datetime, last_updated: datetime):
        self.cursor.execute(f"INSERT INTO {self.table_name} "
                            f"(user_id, nickname, description, photo_id, is_active, create_date, last_updated) "
                            f"VALUES (?, ?, ?, ?, ?, ?, ?);",
                            (user_id, nickname, description, photo_id, is_active, create_date, last_updated, ))

    def get_profile(self, user_id: int) -> Profile:
        self.cursor.execute(f"SELECT DISTINCT * FROM {self.table_name} "
                            f"WHERE user_id=?", (user_id, ))

        data = self.cursor.fetchone()
        if data:
            profile = Profile.Profile(user_id, data[2], data[3], data[4], data[5], data[6], data[7])
            return profile

        return None

    def deactivate_profile(self, uid: [int | str]):
        self.cursor.execute(f"UPDATE {self.table_name} "
                            f"SET is_active=?, last_updated=?"
                            f"WHERE user_id=?", (False, datetime.now(), uid, ))

        self.connection.commit()

    def activate_profile(self, uid: [int | str]):
        self.cursor.execute(f"UPDATE {self.table_name} "
                            f"SET is_active=?, last_updated=?"
                            f"WHERE user_id=?", (True, datetime.now(), uid, ))

        self.connection.commit()

    def create_table(self):
        self.cursor.execute(f"CREATE TABLE {self.table_name} ("
                            f"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            f"user_id INTEGER NOT NULL,"
                            f"nickname varchar(255),"
                            f"description TEXT,"
                            f"photo_id TEXT,"
                            f"is_active BOOL,"
                            f"create_date DATETIME,"
                            f"last_updated DATETIME);")
        
        self.connection.commit()
        

class UniversitiesTable(BaseTable):
    def __init__(self, path: str, table_name: str):
        super().__init__(path, table_name)

    def create_table(self):
        self.cursor.execute(f"CREATE TABLE {self.table_name} ("
                            f"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            f"name varchar(255),"
                            f"domain varchar(255));")
        
        self.connection.commit()

    def __add_university(self):
        self.cursor.execute(f"INSERT INTO {self.table_name} (name, domain)"
                            f"VALUES (?, ?)", ("NU", "nu.edu.kz", ))
        self.cursor.execute(f"INSERT INTO {self.table_name} (name, domain)"
                            f"VALUES (?, ?)", ("AITU", "aitu.edu.kz", ))
        self.connection.commit()
