from dataclasses import dataclass
from os import environ


@dataclass
class TgBot:
    token: str


def load_config():
    return TgBot(
        token=environ["TG_BOT_TOKEN"],
    )
