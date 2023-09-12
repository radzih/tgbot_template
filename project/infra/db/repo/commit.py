from project.core.shared import interace

from .base import BaseRepo


class Commiter(BaseRepo, interace.Commiter):
    async def commit(self) -> None:
        await self._session.commit()
