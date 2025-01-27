# Individual API tests (optional)
import json
from urllib.parse import urljoin

from tests.fixtures.auth_fixtures import *
from tests.utils import *

def test_individual_api(superuser_token):
    
    print(superuser_token)


def test_create_api(get_env_data, get_endpoints):
    
    params = { "tenantId": get_env_data["stateCode"]+"."+get_env_data["cityCode"] }

    with open("tests/data/payload/pgr/create.json") as f:
        body = json.load(f)

    URL = urljoin(get_env_data["host"], get_endpoints["pgr-services"]["pgr-services"])
    
    response = api_utils.make_request(method="POST", url=URL, 
                                    params=params, payload=body)

    print(response.json())