from aiogram import Bot, Dispatcher

from project.config import configure_logging, load_config
from project.infra.db.main import create_connection_url, create_session_factory
from project.present.bot.handlers.setup import include_routers
from project.present.bot.locales.main import create_translator_hub
from project.present.bot.middlewares.setup import setup_middlewares


async def main() -> None:
    config = load_config()
    configure_logging(config.debug)

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    connection_url = create_connection_url(config.db, async_=True)
    session_factory = create_session_factory(connection_url)

    translator_hub = create_translator_hub()

    include_routers(dp)
    setup_middlewares(dp, session_factory, translator_hub)

    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
