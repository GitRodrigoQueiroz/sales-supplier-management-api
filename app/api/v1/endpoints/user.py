from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.schemas import User
from app.services.auth_service import get_current_user
from app.services.db_service import get_session
from app.services.user import UserUseCases

route = APIRouter(prefix="/user")


@route.post("/create")
def user_register(
    user: User,
    session: Session = get_session,
):
    uc = UserUseCases(db_session=session)
    uc.user_register(user=user)
    return {"message": "User registered successfully"}


@route.post("/login")
def user_login(
    user: dict = get_current_user,
    # session: Session = get_session,
):
    return user
    # uc = UserUseCases(db_session=session)
    # uc.user_login(user=user)


@route.post("/logout")
def user_logout(
    user: User,
    session: Session = get_session,
):
    pass


@route.delete("/delete")
def user_delete(
    user: User,
    session: Session = get_session,
):
    pass
