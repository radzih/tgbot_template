from aiogram import Dispatcher
from fluentogram import TranslatorHub
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .i18n import I18nMiddleware
from .interactor import InteractorMiddleware


def setup_middlewares(
    dp: Dispatcher,
    session_factory: async_sessionmaker[AsyncSession],
    tranalator_hub: TranslatorHub,
):
    dp.update.middleware(InteractorMiddleware(session_factory))
    dp.update.middleware(I18nMiddleware(tranalator_hub))
