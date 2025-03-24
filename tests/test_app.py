import pytest

from app import app


@pytest.fixture
def client():
    """Creates a test client for the Flask app."""
    app.testing = True
    return app.test_client()

def test_hello_world(client):
    """Tests the hello_world endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
