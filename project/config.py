from dataclasses import dataclass
from logging import DEBUG, INFO, basicConfig

from project.infra.db.config import Database
from project.infra.db.config import load_config as load_db_config
from project.present.bot.config import TgBot
from project.present.bot.config import load_config as load_bot_config


@dataclass
class Config:
    tg_bot: TgBot
    db: Database
    debug: bool = False


def load_config():
    return Config(
        tg_bot=load_bot_config(),
        db=load_db_config(),
        debug=True,
    )


def configure_logging(debug: bool) -> None:
    basicConfig(level=DEBUG if debug else INFO)
