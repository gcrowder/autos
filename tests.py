from apistar.test import TestClient
from app import app, welcome, create_auto
from apistar.backends.sqlalchemy_backend import Session
import json


def test_welcome():
    """
    Testing a view directly.
    """
    data = welcome()
    assert data == {'message': 'Welcome to API Star!'}


def test_http_request():
    """
    Testing a view, using the test client.
    """
    client = TestClient(app)
    response = client.get('http://localhost/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to API Star!'}


def test_create_auto_request():
    """
    Test create_auto view
    """
    gregs_porsche = {
        "name": "Greg's Porsche",
        "make": "Porsche",
        "model": "911 Turbo",
        "year": "1992"
    }
    client = TestClient(app)
    response = client.post('http://localhost/autos', json=gregs_porsche)
    assert response.status_code == 200
    response_dict = response.json()
    gregs_porsche["id"] = response_dict["id"]
    assert response_dict == gregs_porsche