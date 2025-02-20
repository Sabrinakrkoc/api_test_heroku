import pytest
from apitest.config.settings import BASE_URL, USERNAME, PASSWORD
from apitest.config.login_config import HEADERS, get_auth_payload
from apitest.utils.request_helper import post_request

@pytest.mark.auth
def test_valid_auth():
    """Validate auth was succesfull"""
    url = f"{BASE_URL}/auth"
    payload = get_auth_payload(USERNAME, PASSWORD)
    response = post_request(url, payload, HEADERS)

    assert response.status_code == 200, f"Error: {response.text}"
    assert "token" in response.json(), "No token found"
