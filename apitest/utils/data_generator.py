import random

def get_booking_payload():
    """Generates a dynamic booking payload."""
    return {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": random.randint(50, 500),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-20",
            "checkout": "2025-02-25"
        },
        "additionalneeds": "Breakfast"
    }

updated_booking_details = {
    "firstname": "John",
    "lastname": "Doe",
    "totalprice": 500,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-02-20",
        "checkout": "2025-02-28"
    },
    "additionalneeds": "Breakfast"
}
