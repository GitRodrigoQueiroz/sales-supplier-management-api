from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import User as UserModel
from app.schemas import User
from app.session import ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")
cripto_ctx = CryptContext(schemes=["sha256_crypt"])


def check_token_exp(exp: timedelta):
    if datetime.fromtimestamp(exp, timezone.utc) <= datetime.utcnow().replace(
        tzinfo=timezone.utc
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Expired Token",
        )


@Depends
def get_payload(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token",
            )
        return {
            "username": payload.get("sub"),
            "exp": payload.get("exp", datetime.utcnow()),
        }
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
        )


class AuthService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def authenticate(
        self,
        username: str,
        password: str,
    ):
        user = (
            self.db_session.query(UserModel)
            .filter_by(
                user_name=username,
            )
            .first()
        )
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )
        if not cripto_ctx.verify(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        return user

    def create_access_token(
        self,
        data: dict,
        expires_delta: Optional[timedelta] = None,
    ):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def register_user(self, user: User):
        user_hashed = UserModel(
            user_name=user.user_name,
            password=cripto_ctx.hash(user.password),
            is_admin=False,
        )
        try:
            self.db_session.add(user_hashed)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="user already exists",
            )
