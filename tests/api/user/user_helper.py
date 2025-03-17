from utils import api_utils


def login(username, password, tenantId, type, 
                     headers = api_utils.get_env_data()["auth_header"]):
    """Test valid login"""
    url = api_utils.build_url(api_utils.get_env_data()["host"], 
                  api_utils.get_endpoints("user")["oauth"])

    body = {
              "username": username,
              "password": password,
              "grant_type": "password",
              "scope": "read",
              "tenantId": tenantId,
              "userType": type
            }
    
    header = headers

    response = api_utils.make_request("POST", url, payload=body, headers=header, is_json=False)
    return response