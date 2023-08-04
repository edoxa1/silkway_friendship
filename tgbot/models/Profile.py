from datetime import datetime


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

    def generate_text(self) -> str:
        text = f"{self.nickname}\n" \
               f"{self.description}\n"

        return text
