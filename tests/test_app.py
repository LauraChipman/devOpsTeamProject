import pytest
from app import app

@pytest.fixture
def client():
    """Set up the Flask test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route."""
    response = client.get("/")
    assert response.status_code == 200

def test_get_weather_missing_city(client):
    """Test the /get_weather endpoint with no city provided."""
    response = client.post("/get_weather", json={})
    assert response.status_code == 400
    assert response.json == {"error": "City not provided"}

def test_get_weather_invalid_city(client, requests_mock):
    """Test the /get_weather endpoint with an invalid city."""

    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather?q=InvalidCity&units=metric&appid=8117ef82349de9509894acdad6bb6261",
        status_code=404
    )
    response = client.post("/get_weather", json={"city": "InvalidCity"})
    assert response.status_code == 404
    assert response.json == {"error": "City not found"}
