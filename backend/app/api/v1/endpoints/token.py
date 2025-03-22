from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.app.services.db_service import get_session
from backend.app.services.user_service import UserUseCases
from backend.app.session import ACCESS_TOKEN_EXPIRE_MINUTES

route = APIRouter()


@route.post("/login")
def login_for_access_token(
    session: Session = get_session,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = UserUseCases(session)
    user_db = user.authenticate_user(
        form_data.username,
        form_data.password,
    )
    access_token = user.create_access_token(
        data={"sub": user_db.user_name},
        expires_delta=timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)),
    )
    return {"access_token": access_token, "token_type": "bearer"}
