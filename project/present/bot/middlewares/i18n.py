from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from fluentogram import TranslatorHub


class I18nMiddleware(BaseMiddleware):
    def __init__(self, hub: TranslatorHub) -> None:
        self.hub = hub

    async def __call__(
        self,
        handler: Callable[
            [TelegramObject, Dict[str, Any]],
            Awaitable[Any],
        ],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        data["i18n"] = self.hub.get_translator_by_locale("en")

        return await handler(event, data)
