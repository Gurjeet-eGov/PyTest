# Individual API tests (optional)
import json, allure
from urllib.parse import urljoin

from tests.fixtures.auth_fixtures import *
from tests.utils import *
from tests.data.payload.common import workflow_action
from tests.data.payload.pgr import create

@allure.feature("Login Feature")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_individual_api(superuser_token):
    
    print(superuser_token)


@allure.feature("PGR Feature")
@allure.story("Invalid Create")
@allure.severity(allure.severity_level.NORMAL)
def test_create_api(superuser_token, get_env_data, get_endpoints):
    
    ReqInfo = superuser_token

    Workflow = workflow_action.Workflow(action="APPLY")
    
    params = { "tenantId": get_env_data["stateCode"]+"."+get_env_data["cityCode"] }

    with open("tests/data/payload/pgr/create.json") as f:
        service_json = json.load(f)

    Service = create.Service.model_validate(service_json)

    payload_data = create.Model(service=Service, workflow=Workflow, RequestInfo=ReqInfo).model_dump()

    URL = urljoin(get_env_data["host"], get_endpoints["pgr-services"]["create"])
    
    response = api_utils.make_request(method="POST", url=URL, 
                                    params=params, payload=payload_data)

    print(response.json())

