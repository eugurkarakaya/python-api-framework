from unittest.mock import Mock,patch
from api.client import get,post,put,delete

def test_get_mock(fake_crud_response):

    with patch("api.client.session.request",return_value=fake_crud_response):
        response = get("/posts/1")

        assert response.status_code == 200

        data = response.json()

        assert data["id"] == 1
        assert data["title"] == "API Test"
        assert data["userId"] == 1

def test_post_mock(fake_crud_response):

    fake_crud_response.status_code = 201
    fake_crud_response.json.return_value = {
        "id": 101,
        "title": "API Test",
        "body": "Learning Python",
        "userId": 1
    }

    payload = {
        "title": "API Test",
        "body": "Learning Python",
        "userId": 1}

    with patch("api.client.session.request",return_value=fake_crud_response):
        response = post("/posts/add",payload)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "API Test"
        assert data["userId"] == 1
        assert data["body"] == "Learning Python"

def test_put_mock(fake_crud_response):


    fake_crud_response.json.return_value = {
        "id": 1,
        "title": "Updated API Test",
        "body": "Updated body",
        "userId": 1
    }

    payload = {
        "title": "Updated API Test",
        "body": "Updated body",
        "userId": 1
    }

    with patch(
        "api.client.session.request",
        return_value=fake_crud_response
    ):
        response = put("/posts/1", payload)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Updated API Test"
    assert data["body"] == "Updated body"

def test_delete_mock(fake_crud_response):

    fake_crud_response.json.return_value["isDeleted"] = True

    with patch(
        "api.client.session.request",
        return_value=fake_crud_response
    ):
        response = delete("/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["isDeleted"] is True