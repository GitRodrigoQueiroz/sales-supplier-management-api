from datetime import datetime, timedelta
from typing import Optional

from fastapi import status
from fastapi.exceptions import HTTPException
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import User as UserModel
from app.schemas import User
from app.session import ALGORITHM, SECRET_KEY

cripto_ctx = CryptContext(schemes=["sha256_crypt"])


class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def authenticate_user(
        self,
        username: str,
        password: str,
    ):
        user_on_db = (
            self.db_session.query(UserModel)
            .filter_by(
                user_name=username,
            )
            .first()
        )
        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )
        if not cripto_ctx.verify(password, user_on_db.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        return user_on_db

    def create_access_token(
        self,
        data: dict,
        expires_delta: Optional[timedelta] = None,
    ):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

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
