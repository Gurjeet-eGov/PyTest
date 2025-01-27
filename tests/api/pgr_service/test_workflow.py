# Workflow tests

import pytest
from tests.utils.api_utils import make_request
from tests.utils.validations import validate_response_status

# def test_business_workflow(base_url, get_auth_token):
#     headers = {"Authorization": f"Bearer {get_auth_token}"}

#     # Step 1: Call API 1
#     url1 = f"{base_url}/endpoint1"
#     payload1 = {"key": "value"}
#     response1 = make_request("POST", url1, headers=headers, payload=payload1)
#     validate_response_status(response1)

#     # Step 2: Call API 2 using data from API 1
#     extracted_data = response1["data"]["key"]
#     url2 = f"{base_url}/endpoint2"
#     payload2 = {"dependent_key": extracted_data}
#     response2 = make_request("POST", url2, headers=headers, payload=payload2)
#     validate_response_status(response2)

#     # Continue for subsequent steps as needed
