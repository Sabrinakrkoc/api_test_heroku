import pytest
from apitest.config.settings import BASE_URL, HEADERS, get_auth_token
from apitest.utils.request_helper import put_request
from apitest.utils.data_generator import get_booking_payload
from apitest.utils.request_helper import post_request


@pytest.mark.booking
def test_update_booking():
    """Verify booking update."""
    # Get token
    token = get_auth_token()

    # Update header
    headers_with_token = HEADERS.copy()
    headers_with_token["Cookie"] = f"token={token}"

    # 1. Create reserve to get booking id.
    url_create = f"{BASE_URL}/booking"
    payload = get_booking_payload()
    response_create = post_request(url_create, payload, headers_with_token)

    assert response_create.status_code == 200, f"Error creating booking: {response_create.text}"
    booking_id = response_create.json().get("bookingid")
    assert booking_id, "Booking ID not returned"

    # 2. Upfate reserve
    url_update = f"{BASE_URL}/booking/{booking_id}"
    updated_payload = get_booking_payload()
    response_update = put_request(url_update, updated_payload, headers_with_token)

    assert response_update.status_code == 200, f"Error updating booking: {response_update.text}"
