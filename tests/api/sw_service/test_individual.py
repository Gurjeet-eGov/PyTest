# Individual API tests (optional)
import json, allure
from urllib.parse import urljoin

from utils import api_utils
from data.payload.common import workflow_action
from data.payload.sw import create


@allure.feature("SW Feature")
@allure.story("Valid Create")
@allure.severity(allure.severity_level.NORMAL)
def test_create_api(get_reqInfo, get_env_data, get_endpoints):
    
    ReqInfo = get_reqInfo["Superuser"]
    
    params = { "tenantId": get_env_data["stateCode"]+"."+get_env_data["cityCode"] }

    with open("data/constants/sw/create.json") as f:
        service_json = json.load(f)

    Service = create.SewerageConnection.model_validate(service_json)

    payload_data = create.Model(SewerageConnection=Service, RequestInfo=ReqInfo).model_dump()

    URL = urljoin(get_env_data["host"], get_endpoints["sw-services"]["create"])
    
    response = api_utils.make_request(method="POST", url=URL, 
                                    params=params, payload=payload_data)

    print(response.json())
    assert response.status_code == 200
    # assert response.json()["status"] == "successful"
    # assert response.json()["ServiceWrappers"][0]["service"]["active"] is True

    return response.json()

@allure.feature("SW Feature")
@allure.story("Submit SW Create")
@allure.severity(allure.severity_level.NORMAL)
def test_update_api(get_reqInfo, get_env_data, get_endpoints):
    
    ReqInfo = get_reqInfo["Superuser"]
    
    params = { "tenantId": get_env_data["stateCode"]+"."+get_env_data["cityCode"] }

    with open("data/constants/sw/create.json") as f:
        service_json = json.load(f)

    Service = create.SewerageConnection.model_validate(service_json)

    payload_data = create.Model(SewerageConnection=Service, RequestInfo=ReqInfo).model_dump()

    URL = urljoin(get_env_data["host"], get_endpoints["sw-services"]["create"])
    
    response = api_utils.make_request(method="POST", url=URL, 
                                    params=params, payload=payload_data)

    print(response.json())
    assert response.status_code == 200
    # assert response.json()["status"] == "successful"
    # assert response.json()["ServiceWrappers"][0]["service"]["active"] is True

    return response.json()

