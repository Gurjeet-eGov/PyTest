# Echallan API tests (template)
import json
import allure
from urllib.parse import urljoin

from tests.fixtures.auth_fixtures import *
from utils import api_utils
from data.payload.common import workflow_action
from data.payload.echallan import create as echallan_create


@allure.feature("EChallan Feature")
@allure.story("Individual Echallan Create")
@allure.severity(allure.severity_level.NORMAL)
def test_echallan_create(superuser_token, get_env_data, get_endpoints):
	"""Template test for creating an echallan. Update endpoints and payload as needed."""

	ReqInfo = superuser_token

	Workflow = workflow_action.Workflow(action="APPLY")

	params = {"tenantId": get_env_data["stateCode"] + "." + get_env_data["cityCode"]}

	# Load sample payload (you can replace with your canonical JSON)
	with open("data/constants/echallan/create.json") as f:
		service_json = json.load(f)

	Service = echallan_create.Service.model_validate(service_json["service"]) if hasattr(echallan_create.Service, 'model_validate') else echallan_create.Service(**service_json["service"])

	payload_data = echallan_create.Model(service=Service, workflow=Workflow, RequestInfo=ReqInfo).model_dump()

	# Build URL - update service key in endpoints.json to point to echallan service
	URL = urljoin(get_env_data["host"], get_endpoints.get("echallan", {}).get("create", "/echallan/_create"))

	response = api_utils.make_request(method="POST", url=URL, params=params, payload=payload_data)

	# Defensive handling: make sure we have a Response-like object
	try:
		status_code = response.status_code
		body = response.json()
	except Exception:
		# If response is an error dict, assert accordingly
		assert False, f"Request failed or returned non-HTTP response: {response}"

	print(body)

	assert status_code in (200, 201)
	# Add additional asserts depending on your API contract

	return body
