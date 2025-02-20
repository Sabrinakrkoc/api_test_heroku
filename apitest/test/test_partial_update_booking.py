from apitest.config.settings import BASE_URL
from apitest.config.settings import BASE_URL, HEADERS, get_auth_token
from apitest.utils.data_generator import get_booking_payload
from apitest.utils.request_helper import get_request, post_request, patch_request

def test_partial_update_booking():
    """Partial update."""
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
    updated_payload = {"firstname": "UpdatedFirstName"}
    response_update = patch_request(url_update, updated_payload, headers_with_token)

    assert response_update.status_code == 200, f"Error updating booking: {response_update.text}"

    response_retrieve = get_request(url_update, headers_with_token)
    assert response_retrieve.status_code == 200, f"Error retrieving booking: {response_retrieve.text}"

    booking_data = response_retrieve.json()
    assert booking_data['firstname'] == "UpdatedFirstName", f"Expected firstname to be 'UpdatedFirstName', but got {booking_data['firstname']}"
    assert booking_data['lastname'] == payload['lastname'], f"Expected lastname to be unchanged, but got {booking_data['lastname']}"
