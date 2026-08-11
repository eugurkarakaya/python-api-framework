from unittest.mock import Mock,patch
from api.client import login,session,me


def test_login_mock(fake_login_response):

    with patch("api.client.session.request",return_value=fake_login_response):
        response = login("emily", "emiliypass")
        assert response.status_code == 200
        data=response.json()

        assert "accessToken" in data
        assert "refreshToken" in data

        assert session.headers["Authorization"] == f"Bearer fake-access-token"

def test_current_user_mock(fake_login_response,fake_me_response):

    with patch(
        "api.client.session.request",
        side_effect=[fake_login_response, fake_me_response]):

        login("emilys", "emilys")
        response=me()
        assert response.status_code == 200
        data=response.json()
        assert "id" in data
        assert "username" in data