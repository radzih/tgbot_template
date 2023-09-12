from typing import Protocol

from ..user.model import User


class UserRepo(Protocol):
    async def get_user(self, user_id: int) -> User | None:
        ...

    async def save_user(self, user: User) -> bool:
        ...

    async def get_users(self) -> list[User]:
        ...


class Commiter(Protocol):
    async def commit(self) -> None:
        ...
