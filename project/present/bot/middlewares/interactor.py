from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from project.core.user import interactor
from project.infra.db.main import DBGateway


class InteractorMiddleware(BaseMiddleware):
    def __init__(
        self, session_factory: async_sessionmaker[AsyncSession]
    ) -> None:
        self.session_factory = session_factory

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        db_session = self.session_factory()

        db_gateway = DBGateway(db_session)

        data["create_user"] = interactor.CreateUser(db_gateway)

        try:
            await handler(event, data)
        finally:
            await db_session.close()
