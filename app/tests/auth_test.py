from fastapi import status

from app.tests.conftest_ import client


def get_auth_token_admin(
    client,
    username="admin",
    password="admin",
):
    """Obtém um token JWT válido para testes"""
    response = client.post(
        "/v1/auth/login",
        data={"username": username, "password": password},
    )
    assert response.status_code == status.HTTP_200_OK
    json_data = response.json()
    return json_data["access_token"]


def test_login_admin(client):
    """Testa se o admin consegue logar e obter um token JWT"""
    token = get_auth_token_admin(client)
    assert token is not None
    assert isinstance(token, str)


def test_login_user1(client):
    """Testa o login do usuário 1"""
    response = client.post(
        "v1/auth/login",
        data={
            "username": "user1",
            "password": "user1",
        },
    )

    assert response.status_code == status.HTTP_200_OK
    json_data = response.json()
    assert "access_token" in json_data
    assert json_data["token_type"] == "bearer"


def test_login_invalid_user(client):
    """Testa o login de um usuário inexistente."""
    response = client.post(
        "v1/auth/login",
        data={
            "username": "admin",
            "password": "password_incorrect",
        },
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_register_user(client):
    """Testa o cadastro de um novo usuário."""
    new_user = {
        "user_name": "novousuario",
        "password": "senha123",
    }

    response = client.post(
        "v1/auth/register_user",
        json=new_user,
    )
    assert response.status_code == 200


def test_delete_user(client):
    """Testa uma rota protegida por JWT (delete_user)"""

    # Obtém o token de autenticação
    token = get_auth_token_admin(client)

    # Faz uma requisição à rota protegida com o token no cabeçalho
    response = client.delete(
        "/v1/auth/delete_user/2",  # Substitua pela rota que deseja testar
        headers={"Authorization": f"Bearer {token}"},
    )

    # Verifica se o acesso foi autorizado
    assert response.status_code == 200
