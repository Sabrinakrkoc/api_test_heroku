import pytest
from apitest.config.settings import BASE_URL
from apitest.config.login_config import HEADERS, get_auth_payload
from apitest.utils.request_helper import post_request

@pytest.mark.auth
def test_invalid_auth():
    """Validate auth fails with invalid credentials (403 Forbidden)"""
    url = f"{BASE_URL}/auth"
    payload = get_auth_payload("wrong_user", "wrong_pass")
    response = post_request(url, payload, HEADERS)

    assert response.status_code == 403, f"Expected 403, got {response.status_code}, response: {response.text}"
