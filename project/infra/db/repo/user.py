from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from project.core.shared import interace
from project.core.user import model as core_model
from project.core.user.dto import UserCreate

from ..models.user import User
from .base import BaseRepo


class UserRepo(BaseRepo, interace.UserRepo):
    async def save_user(self, user: core_model.User) -> bool:
        user = User(id=user.id, name=user.name, created_time=user.created_time)
        self._session.add(user)

        try:
            await self._session.flush()
        except IntegrityError as e:
            await self._session.rollback()
            return False
        return True

    async def get_user(self, user_id: int) -> core_model.User | None:
        user = await self._session.get(User, user_id)
        if not user:
            return None
        return core_model.User(
            id=user.id,
            name=user.name,
            created_date=user.created_time,
        )

    async def get_users(self) -> list[core_model.User]:
        query = select(User)

        users = await self._session.execute(query)
        return [
            core_model.User(
                id=user.id,
                name=user.name,
                created_date=user.created_time,
            )
            for user in users.scalars()
        ]
