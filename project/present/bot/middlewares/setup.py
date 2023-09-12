from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .interactor import InteractorMiddleware


def setup_middlewares(
    dp: Dispatcher,
    session_factory: async_sessionmaker[AsyncSession],
):
    dp.update.middleware(InteractorMiddleware(session_factory))
