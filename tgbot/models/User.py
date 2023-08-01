from tgbot.models import Profile
from typing import List

from tgbot.models.Enums import University


class User:
    def __init__(self, uid: int, university: University, is_verified: bool, is_banned: bool, verification_code: int) -> None:
        self.uid: int = uid
        self.university: University = university
        self.is_verified: bool = is_verified
        self.is_banned: bool = is_banned
        self.verification_code = verification_code

        self.user_buffer: List[int] = []
        self.profile: Profile

    def info(self) -> str:
        text = f"{self.uid} {self.university.name} {self.verification_code}"
        return text

    def create_profile(self) -> Profile:
        pass

    def ban(self) -> bool:
        pass
 
    def verify(self) -> bool:
        pass
