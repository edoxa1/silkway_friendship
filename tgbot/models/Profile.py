from datetime import datetime
from tgbot.services.database import Database


class Profile:
    def __init__(self, uid: int, nickname: str, description: str,
                 photo_id: str, is_active: bool,
                 create_date: datetime, update_date: datetime) -> None:
        self.uid: int = uid
        self.nickname: str = nickname
        self.description: str = description
        self.photo_id: str = photo_id
        self.is_active: bool = is_active
        self.create_date: datetime = create_date
        self.update_date: datetime = update_date
        self.db: Database = Database.get_instance()

    def generate_text(self) -> str:
        text = f"{self.nickname}\n" \
               f"{self.description}\n" \
               f"Your profile is {'active' if self.is_active else 'deactivated'}"

        return text

    def activate(self):
        self.is_active = True
        self.db.profiles_table.update_column(self.uid, "is_active", self.is_active)

    def deactivate(self):
        self.is_active = False
        self.db.profiles_table.update_column(self.uid, "is_active", self.is_active)

    def change_nickname(self, nickname: str):
        self.nickname = nickname
        self.db.profiles_table.update_column(self.uid, "nickname", self.nickname)

    def change_description(self, description: str):
        self.description = description
        self.db.profiles_table.update_column(self.uid, "description", self.description)

    def change_photo_id(self, photo_id: str):
        self.photo_id = photo_id
        self.db.profiles_table.update_column(self.uid, "photo_id", self.photo_id)
