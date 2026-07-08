from fastapi.testclient import TestClient #fast api special tool for testing
from main import app

client = TestClient(app)

def test_get_jobs():
    response = client.get("/jobs")
    assert response.status_code == 200
