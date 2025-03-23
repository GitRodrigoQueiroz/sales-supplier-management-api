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


def test_create_location(client):
    """Testa uma rota protegida por JWT (delete_user)"""

    # Obtém o token de autenticação
    token = get_auth_token_admin(client)

    response = client.post(
        "/v1/crud/location/create",
        headers={"Authorization": f"Bearer {token}"},
        json=[
            {
                "market": "Ceara",
                "country": "Brasil",
                "province": "America",
                "city": "Quixada",
            }
        ],
    )

    # Verifica se o acesso foi autorizado
    assert response.status_code == 200
