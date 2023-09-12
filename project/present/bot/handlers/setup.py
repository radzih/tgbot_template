from aiogram import Dispatcher

from . import start


def include_routers(dp: Dispatcher):
    dp.include_router(start.router)
