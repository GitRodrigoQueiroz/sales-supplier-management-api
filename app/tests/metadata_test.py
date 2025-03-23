from fastapi import status

from app.tests.conftest_ import client


def test_get_supplier_by_id_metadata(client):
    """Testa o metadata do supplier 1"""
    response = client.get(
        "v1/metadata/supplier/get_by_id/1",
    )

    expected_data = {
        "supplier": {
            "supplier_id": 1,
            "location_id": 1,
            "supplier_name": "AutoParts Inc.",
        },
        "location": {
            "country": "USA",
            "market": "north america",
            "city": "Los Angeles",
            "location_id": 1,
            "province": "California",
        },
    }

    assert response.status_code == status.HTTP_200_OK
    json_data = response.json()
    assert json_data == expected_data


def test_get_part_by_id_metadata(client):
    """Testa o metadata do part 1"""
    response = client.get(
        "v1/metadata/part/get_by_id/1",
    )

    expected_data = {
        "part": {
            "part_name": "Fuel Pump",
            "supplier_id": 1,
            "unit_price": 150,
            "part_id": 1,
        },
        "supplier": {
            "supplier_id": 1,
            "supplier_name": "AutoParts Inc.",
            "location_id": 1,
        },
    }

    assert response.status_code == status.HTTP_200_OK
    json_data = response.json()
    assert json_data == expected_data
