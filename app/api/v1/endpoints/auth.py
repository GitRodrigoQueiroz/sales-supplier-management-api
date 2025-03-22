from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas import User
from app.services.auth import AuthService
from app.services.db_service import get_session
from app.session import ACCESS_TOKEN_EXPIRE_MINUTES

route = APIRouter(prefix="/auth", tags=["Auth"])


@route.post("/register")
def user_register(
    user: User,
    session: Session = get_session,
):
    auth = AuthService(db_session=session)
    auth.user_register(user=user)
    return {"message": "User registered successfully"}


@route.post("/login")
def login(
    session: Session = get_session,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    auth = AuthService(session)
    user = auth.authenticate(
        form_data.username,
        form_data.password,
    )
    access_token = auth.create_access_token(
        data={"sub": user.user_name},
        expires_delta=timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)),
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
