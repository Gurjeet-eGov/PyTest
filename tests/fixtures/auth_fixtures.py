# Common fixtures (e.g., authentication tokens)
import pytest

from tests.utils import api_utils

@pytest.fixture(scope="module")
def citizen_token():
    return api_utils.get_reqInfo("Citizen")

@pytest.fixture(scope="module")
def alt_citizen_token():
    return api_utils.get_reqInfo("alternateCitizen")

@pytest.fixture(scope="module")
def architect_token():
    return api_utils.get_reqInfo("citizenArchitect")

@pytest.fixture(scope="module")
def superuser_token():
    return api_utils.get_reqInfo("Superuser")