import pytest
import requests
from config import USERNAME, PASSWORD
from api.client import login,me,get
from test_data.auth_data import LOGIN_CASES


@pytest.mark.parametrize("username, password, expected_status",LOGIN_CASES)

def test_login(username,password,expected_status):
    response = login(username,password)
    assert response.status_code ==expected_status

    if expected_status ==200:
        data=response.json()
        assert "accessToken" in data
        assert "refreshToken" in data


def test_get_current_user(authenticated):
    response=me()
    data=response.json()
    assert response.status_code == 200
    assert "id" in data
    assert "username" in data
    assert "email" in data

def test_invalid_endpoint():
    response= get("/auth/does-not-exist")
    assert response.status_code == 404

def test_server_error():
    response = get("/http/500")
    assert response.status_code == 500

def test_timeout(authenticated):
    with pytest.raises(requests.exceptions.Timeout):
        get("/auth/me",timeout=0.001)