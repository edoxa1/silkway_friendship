from tgbot.models import Profile
from typing import List


class User:
    def __init__(self, id: str, username: str, first_last_name: str,
                 profile: Profile, is_verified: bool, is_banned: bool,
                 user_buffer: List[str]) -> None:
        self.id: str = id
        self.username: str = username
        self.first_last_name: str = first_last_name
        self.profile: Profile = profile
        self.is_verified: bool = is_verified
        self.is_banned: bool = is_banned
        self.user_buffer: List[str] = user_buffer

    def info(self) -> str:
        pass

    def create_profile(self) -> Profile:
        pass

    def ban(self) -> bool:
        pass
 
    def verify(self) -> bool:
        pass
