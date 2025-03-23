from fastapi import status

from app.tests.conftest_ import client


def test_get_supplier_by_id_metadata(client):
    """Testa o total amount do supplier 1"""
    response = client.get(
        "v1/analytcs/purchance/1/total_amount",
    )

    expected_data = {"total_amount": 750}

    assert response.status_code == status.HTTP_200_OK
    json_data = response.json()
    assert json_data == expected_data
