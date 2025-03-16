# Individual API tests (optional)
import json, allure
from urllib.parse import urljoin

from tests.fixtures.auth_fixtures import *
from tests.utils import *
from tests.data.payload.common import workflow_action
from tests.data.payload.pgr import create
from tests.utils import api_utils


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


@allure.feature("Login Feature")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("username, password, tenant, type", 
                         [("8080808000", "123456", "pg", "CITIZEN"),
                          ("8080808001", "123456", "pg", "CITIZEN"),
                          ("PGRSU", "eGov@123", "pg.citya", "EMPLOYEE")])
def test_valid_citizen_login(username, password, tenant, type):
    
    response = login(username, password, tenant, type)

    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()

