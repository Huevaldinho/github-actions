import pytest
from fastapi.testclient import TestClient
import json

from src.app import app

@pytest.fixture
def client(monkeypatch, tmp_path):
    """
    Pytest fixture to create a TestClient for the FastAPI app.

    It uses monkeypatch to replace the MOCKS_FILE path with a temporary file,
    ensuring that tests are isolated and don't affect the actual data file.
    """
    # Create a temporary directory and file for mock data
    temp_data_dir = tmp_path / "data"
    temp_data_dir.mkdir()
    temp_mocks_file = temp_data_dir / "mocks.json"

    # Explicitly create the mock file with initial empty data.
    # This ensures the file exists before the TestClient makes any calls,
    # resolving the FileNotFoundError. The app's on_startup event will
    # find that the file already exists and do nothing, which is fine for testing.
    temp_mocks_file.write_text("{}")

    # Use monkeypatch to point the app's MOCKS_FILE to our temporary file
    monkeypatch.setattr("src.app.MOCKS_FILE", temp_mocks_file)

    with TestClient(app) as test_client:
        yield test_client


def test_health_check(client: TestClient):
    """Tests the /health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_data_initially_empty(client: TestClient):
    """Tests that GET /data initially returns an empty object."""
    response = client.get("/data")
    assert response.status_code == 200
    assert response.json() == {}


def test_update_and_get_data(client: TestClient):
    """
    Tests that POST /data updates the data and that a subsequent
    GET /data returns the updated data.
    """
    # 1. Update the data
    post_response = client.post("/data")
    update = "data_updated"
    assert post_response.status_code == 200
    assert post_response.json() == {
        "message": "Data updated successfully",
        "data": update,
    }

    # 2. Retrieve the data to verify the update
    get_response = client.get("/data")
    assert get_response.status_code == 200
    assert get_response.json() == {"data": update}