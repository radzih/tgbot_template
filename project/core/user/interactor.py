from datetime import datetime

from project.core.shared import interactor

from . import dto, interface, model


class CreateUser(interactor.Interactor):
    def __init__(self, db_gateway: interface.DbGateway):
        self.db_gateway = db_gateway

    async def __call__(self, data: dto.UserCreate) -> bool:
        """
        Create a user.
        Args:
            data (dto.UserCreate): User data.
        Returns:
            bool: True if user is created, False otherwise.
        """
        user = model.User(
            id=data.id, name=data.name, created_time=datetime.now()
        )
        is_saved = await self.db_gateway.save_user(user)
        await self.db_gateway.commit()

        return is_saved
