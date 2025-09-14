# Individual API tests (optional)
import json, allure

from tests.fixtures.auth_fixtures import *
from utils import api_utils
from tests.api.user.user_helper import login


# def login(username, password, tenantId, type, 
#                      headers = api_utils.get_env_data()["auth_header"]):
#     """Test valid login"""
#     url = api_utils.build_url(api_utils.get_env_data()["host"], 
#                   api_utils.get_endpoints("user")["oauth"])

#     body = {
#               "username": username,
#               "password": password,
#               "grant_type": "password",
#               "scope": "read",
#               "tenantId": tenantId,
#               "userType": type
#             }
    
#     header = headers

#     response = api_utils.make_request("POST", url, payload=body, headers=header, is_json=False)
#     return response


@allure.feature("Login Feature")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("username, password, tenant, type", 
                         [("{username}", "{password}", "pg", "CITIZEN"),
                          ("{username}", "{password}", "pg", "CITIZEN"),
                          ("{username}", "{password}", "pg.citya", "EMPLOYEE")])
def test_valid_login(username, password, tenant, type):
    
    response = login(username, password, tenant, type)

    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()


@allure.feature("Login Feature")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("username", ["Citizen", "alternateCitizen", 
                                      "citizenArchitect", "Superuser"])
def test_valid_login_envdata(username):
    creds = api_utils.get_credentials(username)
    response = login(creds["username"], creds["password"],
                     creds["tenantId"], creds["type"])

    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()



csv_user_list = api_utils.get_csv_data("data/constants/user/user_data.csv")
# for entry in csv_user_list:
@allure.feature("Login Feature")
@allure.story("Valid Login (Excel Data)")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("username, password, tenant, type", 
                        [(entry["username"], entry["password"],
                        entry["tenantId"], entry["type"]) for entry in csv_user_list])
def test_valid_login_csv(username, password, tenant, type):
    
    response = login(username, password, tenant, type)

    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()