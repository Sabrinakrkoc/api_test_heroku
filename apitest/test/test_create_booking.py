import pytest
from apitest.config.settings import BASE_URL
from apitest.config.login_config import HEADERS  
from apitest.utils.request_helper import post_request
from apitest.utils.data_generator import get_booking_payload

@pytest.mark.booking
def test_create_booking():
    """Verify creation."""
    url = f"{BASE_URL}/booking"
    payload = get_booking_payload()
    
    # Change `json=payload` to `data=payload` if `post_request` doesn't use`json`
    response = post_request(url, payload, HEADERS)  

    assert response.status_code == 200, f"Error: {response.text}"
    assert "bookingid" in response.json(), "No booking ID returned"
