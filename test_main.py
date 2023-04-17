from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app=app)


def test_user_login():
    response = client.get('/users/me/')

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
