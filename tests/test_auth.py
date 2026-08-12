import pytest
import requests
from api.auth import login,me
from api.client import get
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

@pytest.mark.parametrize("endpoint, expected_status",
                         [
                             ("/auth/does-not-exist",404),
                             ("/http/500",500)
                         ])

def test_endpoint_error(endpoint,expected_status):
    response=get(endpoint)
    assert response.status_code==expected_status

def test_timeout(authenticated):
    with pytest.raises(requests.exceptions.Timeout):
        get("/auth/me",timeout=0.001)