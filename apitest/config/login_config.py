HEADERS = {
    "Content-Type": "application/json"
}

def get_auth_payload(username, password):
    """Devuelve el payload para autenticación"""
    return {"username": username, "password": password}
