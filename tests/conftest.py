import pytest
from api.auth import login
from test_data.auth_data import USERNAME, PASSWORD
import logging
from unittest.mock import Mock, patch

logging.basicConfig(level=logging.INFO)

@pytest.fixture
def authenticated():
    login(USERNAME, PASSWORD)

@pytest.fixture
def fake_login_response():
    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "accessToken": "fake-access-token",
        "refreshToken": "fake-refresh-token"
    }
    return response

@pytest.fixture
def fake_me_response():
    response=Mock()
    response.status_code = 200
    response.json.return_value = {
        "id": 1,
        "username": "emilys"
    }
    return response

@pytest.fixture
def fake_crud_response():
    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "id": 1,
        "title": "API Test",
        "body": "Learning Python",
        "userId": 1
    }
    return response
