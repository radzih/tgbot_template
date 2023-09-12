from sqlalchemy import URL, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker

from project.core.shared.interace import Commiter, UserRepo
from project.core.user.model import User
from project.core.user.model import User as UserCore

from .config import Database
from .models import User


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


class DBGateway(UserRepo, Commiter):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def save_user(self, user: UserCore) -> bool:
        user = User(id=user.id, name=user.name, created_time=user.created_time)
        self._session.add(user)

        try:
            await self._session.flush()
        except IntegrityError as e:
            await self._session.rollback()
            return False
        return True

    async def get_user(self, user_id: int) -> UserCore | None:
        user = await self._session.get(User, user_id)
        if not user:
            return None
        return UserCore(
            id=user.id,
            name=user.name,
            created_date=user.created_time,
        )

    async def get_users(self) -> list[UserCore]:
        query = select(User)

        users = await self._session.execute(query)
        return [
            UserCore(
                id=user.id,
                name=user.name,
                created_date=user.created_time,
            )
            for user in users.scalars()
        ]
