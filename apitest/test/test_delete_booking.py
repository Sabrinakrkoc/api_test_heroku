from apitest.config.settings import BASE_URL
from apitest.config.settings import BASE_URL, HEADERS, get_auth_token
from apitest.utils.data_generator import get_booking_payload
from apitest.utils.request_helper import delete_request, get_request, post_request

def test_delete_booking():
    """Delete reserve."""
    token = get_auth_token()

    # Update header with new token
    headers_with_token = HEADERS.copy()
    headers_with_token["Cookie"] = f"token={token}"

    # 1. Create reserve to get booking id
    url_create = f"{BASE_URL}/booking"
    payload = get_booking_payload()
    response_create = post_request(url_create, payload, headers_with_token)

    assert response_create.status_code == 200, f"Error creating booking: {response_create.text}"
    booking_id = response_create.json().get("bookingid")
    assert booking_id, "Booking ID not returned"

    # 2. Delete reserve using el ID obtain
    url_delete = f"{BASE_URL}/booking/{booking_id}"
    response_delete = delete_request(url_delete, headers_with_token)

    assert response_delete.status_code == 201, f"Expected 201 Created, but got {response_delete.status_code}"

    # 3. Verify reserve doesn't exist
    url_retrieve = f"{BASE_URL}/booking/{booking_id}"
    response_retrieve = get_request(url_retrieve, headers_with_token)

    assert response_retrieve.status_code == 404, f"Expected 404 Not Found, but got {response_retrieve.status_code}"
