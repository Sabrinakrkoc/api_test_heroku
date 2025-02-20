import pytest
from apitest.config.settings import BASE_URL, HEADERS, get_auth_token
from apitest.utils.request_helper import put_request
from apitest.utils.data_generator import get_booking_payload
from apitest.utils.request_helper import post_request


@pytest.mark.booking
def test_unauthorized_update_booking():
    """Verify unauthorized booking update without a valid token."""
    token = get_auth_token()

    headers_with_token = HEADERS.copy()
    headers_with_token["Cookie"] = f"token={token}"

    url_create = f"{BASE_URL}/booking"
    payload = get_booking_payload()
    response_create = post_request(url_create, payload, headers_with_token)

    assert response_create.status_code == 200, f"Error creating booking: {response_create.text}"
    booking_id = response_create.json().get("bookingid")
    assert booking_id, "Booking ID not returned"

    url_update = f"{BASE_URL}/booking/{booking_id}"
    updated_payload = get_booking_payload()

    invalid_headers = headers_with_token.copy()
    invalid_headers["Cookie"] = "token=invalid_token"

    response_update = put_request(url_update, updated_payload, invalid_headers)

    assert response_update.status_code == 403, f"Expected 403 Forbidden, but got {response_update.status_code}. Error: {response_update.text}"
