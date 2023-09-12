from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker

from . import repo
from .config import Database


def create_connection_url(db: Database, async_: bool = False) -> URL:
    return URL.create(
        # todo: change drivers to sqlalchemy vars
        drivername="postgresql+asyncpg" if async_ else "postgresql",
        username=db.user,
        password=db.password,
        host=db.host,
        port=db.port,
        database=db.name,
    )


def create_session_factory(
    url: URL, echo: bool = False
) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(url, echo=echo)
    return async_sessionmaker(bind=engine, class_=AsyncSession)


class DBGateway(repo.UserRepo, repo.Commiter):
    pass
