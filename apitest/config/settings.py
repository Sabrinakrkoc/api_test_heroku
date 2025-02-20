import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
USERNAME = os.getenv("USERNAME", "admin")
PASSWORD = os.getenv("PASSWORD", "password")

def get_auth_token():
    """Get valid token."""
    url = f"{BASE_URL}/auth"
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get("token")
    else:
        raise Exception(f"Failed to authenticate. Status code: {response.status_code}")

TOKEN = get_auth_token()

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": f"token={TOKEN}"
}
