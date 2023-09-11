from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

start = BotCommand(command="start", description="Start bot")

commands = [start]


async def set_commands(bot: Bot, user_id: int) -> None:
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
