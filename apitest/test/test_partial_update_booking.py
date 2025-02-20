from apitest.config.settings import BASE_URL
from apitest.config.settings import BASE_URL, HEADERS, get_auth_token
from apitest.utils.data_generator import get_booking_payload
from apitest.utils.request_helper import get_request, post_request, patch_request

def test_partial_update_booking():
    """Actualizar parcialmente una reserva con un token válido."""
    # Obtener el token de autenticación
    token = get_auth_token()

    # Actualizamos el header con el nuevo token
    headers_with_token = HEADERS.copy()
    headers_with_token["Cookie"] = f"token={token}"

    # 1. Crear una reserva inicial para obtener un booking id
    url_create = f"{BASE_URL}/booking"
    payload = get_booking_payload()
    response_create = post_request(url_create, payload, headers_with_token)

    assert response_create.status_code == 200, f"Error creating booking: {response_create.text}"
    booking_id = response_create.json().get("bookingid")
    assert booking_id, "Booking ID not returned"

    # 2. Actualizar parcialmente la reserva (solo un campo)
    url_update = f"{BASE_URL}/booking/{booking_id}"
    updated_payload = {"firstname": "UpdatedFirstName"}  # Solo modificamos el nombre
    response_update = patch_request(url_update, updated_payload, headers_with_token)

    assert response_update.status_code == 200, f"Error updating booking: {response_update.text}"

    # 3. Verificar que solo el campo modificado ha cambiado
    response_retrieve = get_request(url_update, headers_with_token)
    assert response_retrieve.status_code == 200, f"Error retrieving booking: {response_retrieve.text}"

    booking_data = response_retrieve.json()
    assert booking_data['firstname'] == "UpdatedFirstName", f"Expected firstname to be 'UpdatedFirstName', but got {booking_data['firstname']}"
    assert booking_data['lastname'] == payload['lastname'], f"Expected lastname to be unchanged, but got {booking_data['lastname']}"
