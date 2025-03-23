from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.models.user import User as UserModel
from app.schemas import User
from app.services.auth import AuthService, check_token_exp, get_payload
from app.services.db_service import get_session
from app.session import ACCESS_TOKEN_EXPIRE_MINUTES

route = APIRouter(prefix="/auth", tags=["Auth"])


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
        data={
            "sub": user.user_name,
            "is_admin": False,
        },
        expires_delta=timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)),
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@route.post("/register_user")
def register_user(
    user: User,
    session: Session = get_session,
):
    auth = AuthService(db_session=session)
    auth.register_user(user=user)
    return {"message": "User registered successfully"}


@route.post("/list_users")
def list_users(session: Session = get_session):
    users = session.query(UserModel).filter(UserModel.is_admin == False).all()

    if not users:
        return {"error": "Users not found"}

    # Retorna a lista de usuários
    return [
        {
            "id": user.id,
            "username": user.user_name,
        }
        for user in users
    ]


@route.delete("/delete_user/{user_id}")
def delete_user(
    user_id: int,
    payload: dict = get_payload,
    session: Session = get_session,
):
    check_token_exp(payload.get("exp"))
    user = session.query(UserModel).filter(UserModel.id == user_id).first()

    if not user:
        return {"error": "User not found"}

    # Apenas o admin pode excluir usuários ou o próprio usuário pode se deletar
    if payload["username"] != "admin" and (payload["username"] != user.user_name):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    # Deletar o usuário
    session.delete(user)
    session.commit()

    return {"message": "User deleted successfully"}
