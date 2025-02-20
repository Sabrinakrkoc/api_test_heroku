HEADERS = {
    "Content-Type": "application/json"
}

def get_auth_payload(username, password):
    """Return payload for auth"""
    return {"username": username, "password": password}
