# Reusable validation logic

def validate_response_status(response, expected_status=200):
    assert response.get("status") == expected_status, f"Expected {expected_status}, got {response.get('status')}"

def validate_response_contains_key(response, key):
    assert key in response, f"Key '{key}' not found in response"
