from fastapi import status
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.models import User as UserModel
from backend.app.schemas import User

cripto_ctx = CryptContext(schemes=["sha256_crypt"])


class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def user_register(self, user: User):
        user_hashed = UserModel(
            user_name=user.user_name,
            password=cripto_ctx.hash(user.password),
        )
        try:
            self.db_session.add(user_hashed)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="user already exists",
            )
