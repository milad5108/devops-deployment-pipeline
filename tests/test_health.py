from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_api_status():
    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json() == {
        "service": "devops-deployment-pipeline",
        "environment": "development",
        "status": "running",
    }