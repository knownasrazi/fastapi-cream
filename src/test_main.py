from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["name"] == "fastapi-cream"

def test_create_and_list():
    r = client.post("/items", json={"id": 0, "name": "Test", "price": 9.99})
    assert r.status_code == 200
    assert r.json()["name"] == "Test"
    r = client.get("/items")
    assert len(r.json()) >= 1
