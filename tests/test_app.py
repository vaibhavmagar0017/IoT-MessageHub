import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_status_count_endpoint():
    response = client.get("/status_count/", params={"start_time": 0, "end_time": 9999999999})
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
