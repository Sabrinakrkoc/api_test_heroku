import pytest
from apitest.config.settings import BASE_URL, HEADERS
from apitest.utils.request_helper import get_request
import random

@pytest.mark.booking
def test_invalid_booking():
    """Validate retrieval of a non-existent booking ID returns 404"""

    non_existent_id = random.randint(10000, 99999)
    url = f"{BASE_URL}/booking/{non_existent_id}"
    response = get_request(url, HEADERS)

    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
