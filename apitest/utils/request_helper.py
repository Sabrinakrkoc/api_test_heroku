import requests

def post_request(url, json=None, headers=None):
    """Send a POST request and return the response."""
    return requests.post(url, json=json, headers=headers)

def get_request(url, headers=None):
    """Send a GET request and return the response."""
    return requests.get(url, headers=headers)

def put_request(url, payload, headers):
    """Make a PUT request."""
    try:
        response = requests.put(url, json=payload, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error during PUT request: {e}")
        return e.response

def delete_request(url, headers):
    """Make delete DELETE request."""
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error during DELETE request: {e}")
        return e.response

def patch_request(url, payload, headers):
    """Make PATCH request."""
    try:
        response = requests.patch(url, json=payload, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error during PATCH request: {e}")
        return e.response
