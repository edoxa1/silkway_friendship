from datetime import datetime


class Profile:
    def __init__(self, uid: int, db_id: int, nickname: str, description: str,
                 photo_id: str, is_active: bool,
                 create_date: datetime, update_date: datetime) -> None:
        uid: int = uid
        db_id: int = db_id
        nickname: str = nickname
        description: str = description
        photo_id: str = photo_id
        is_active: bool = is_active
        create_date: datetime = create_date
        update_date: datetime = update_date

    def generate_text(self) -> str:
        pass
    
    def clear(self) -> None:
        pass
    
    def update(self) -> None:
        pass
