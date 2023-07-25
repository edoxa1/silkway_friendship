from datetime import datetime


class Profile:
    def __init__(self, id: str, db_id: int, name: str, description: str,
                 photo_id: str, is_active: bool,
                 create_date: datetime, update_date: datetime) -> None:
        id: str = id
        db_id: int = db_id
        name: str = name
        description: str = description
        photo_id: str = photo_id
        is_active: bool = is_active
        create_date: datetime = create_date
        update_date: datetime = update_date

    def generate_text(self) -> str:
        pass
    
    def clear() -> None:
        pass
    
    def update() -> None:
        pass
