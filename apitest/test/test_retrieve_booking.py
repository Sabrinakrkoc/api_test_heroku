import pytest
from apitest.config.settings import BASE_URL, HEADERS
from apitest.utils.request_helper import post_request, get_request
from apitest.utils.data_generator import get_booking_payload

@pytest.mark.booking
def test_retrieve_booking():
    """Validate booking retrieval by ID"""

    create_url = f"{BASE_URL}/booking"
    payload = get_booking_payload()
    create_response = post_request(create_url, payload, HEADERS)
    
    assert create_response.status_code == 200, f"Error creating booking: {create_response.text}"
    booking_id = create_response.json().get("bookingid")
    assert booking_id, "Booking ID not returned"

    # Get details
    retrieve_url = f"{BASE_URL}/booking/{booking_id}"
    retrieve_response = get_request(retrieve_url, HEADERS)

    assert retrieve_response.status_code == 200, f"Error retrieving booking: {retrieve_response.text}"
    assert retrieve_response.json() == payload, "Booking details do not match"
