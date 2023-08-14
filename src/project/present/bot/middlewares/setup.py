from aio_pika import Connection
from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


def setup_middlewares(
    dp: Dispatcher,
    session_factory: async_sessionmaker[AsyncSession],
):
    pass
