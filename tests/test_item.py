from fastapi.testclient import TestClient


def test_find_all(client_fixture: TestClient):
    response = client_fixture.get("/items")
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 2


def test_find_by_id_正常系(client_fixture: TestClient):
    response = client_fixture.get("/items/1")
    assert response.status_code == 200
    item = response.json()
    assert item["id"] == 1


def test_find_by_id_異常系(client_fixture: TestClient):
    response = client_fixture.get("/items/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_find_by_name_正常系(client_fixture: TestClient):
    response = client_fixture.get("/items/?name=PC1")
    assert response.status_code == 200
    item = response.json()
    assert len(item) == 1
    assert item[0]["name"] == "PC1"


def test_find_by_name_異常系(client_fixture: TestClient):
    response = client_fixture.get("/items/?name=**")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_create(client_fixture:TestClient):
    response = client_fixture.post(
        "/items", 
        json={
            "name": "スマホ", "price": 30000, "description": "test", 
            "category": "ELECTRICAL", "status": "ON_SALE", "stock": 10, "user_id": 1
        }
    )
    assert response.status_code == 201
    item = response.json()
    assert item["id"] == 3
    assert item["name"] == "スマホ"
    assert item["price"] == 30000
    assert item["category"] == "ELECTRICAL"
    assert item["stock"] == 10

    response = client_fixture.get("/items")
    assert len(response.json()) == 3


def test_update_正常系(client_fixture: TestClient):
    response = client_fixture.put("/items/1", json={"name": "スマホ", "price": 30000, "stock": 20})
    assert response.status_code == 200
    item = response.json()
    assert item["name"] == "スマホ"
    assert item["price"] == 30000
    assert item["stock"] == 20


def test_update_異常系(client_fixture: TestClient):
    response = client_fixture.put("/items/10", json={"name": "スマホ", "price": 30000, "stock": 20})
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not updated"


def test_delete_正常系(client_fixture: TestClient):
    response = client_fixture.delete("/items/1")
    assert response.status_code == 200
    response = client_fixture.get("/items")
    assert len(response.json()) == 1


def test_delete_異常系(client_fixture: TestClient):
    response = client_fixture.delete("/items/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not deleted"

