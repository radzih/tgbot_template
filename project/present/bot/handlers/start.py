from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, User
from fluentogram import TranslatorRunner

from project.core.user.dto import UserCreate
from project.core.user.interactor import CreateUser

router = Router()


@router.message(CommandStart(), F.from_user.as_("user"))
async def start(
    message: Message,
    user: User,
    create_user: CreateUser,
    i18n: TranslatorRunner,
) -> None:
    is_created = await create_user(UserCreate(id=user.id, name=user.full_name))
    if is_created:
        await message.answer(i18n.start.registered())
    else:
        await message.answer(i18n.start.already_registered())
