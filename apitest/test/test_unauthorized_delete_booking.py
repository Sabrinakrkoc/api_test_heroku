import pytest
from apitest.config.settings import BASE_URL
from apitest.config.settings import BASE_URL, HEADERS, get_auth_token
from apitest.utils.data_generator import get_booking_payload
from apitest.utils.request_helper import delete_request, post_request

def test_unauthorized_delete_booking():
    """Verify unauthorized booking deletion."""
    token = get_auth_token()

    headers_with_invalid_token = HEADERS.copy()
    headers_with_invalid_token["Cookie"] = "token=invalid_token"

    url_create = f"{BASE_URL}/booking"
    payload = get_booking_payload()
    response_create = post_request(url_create, payload, headers_with_invalid_token)
    
    assert response_create.status_code == 200, f"Error creating booking: {response_create.text}"
    booking_id = response_create.json().get("bookingid")
    assert booking_id, "Booking ID not returned"

    url_delete = f"{BASE_URL}/booking/{booking_id}"
    response_delete = delete_request(url_delete, headers_with_invalid_token)

    # Validate fail
    assert response_delete.status_code == 403, f"Expected 403 Forbidden, but got {response_delete.status_code}. Error: {response_delete.text}"

