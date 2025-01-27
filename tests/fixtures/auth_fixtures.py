# Common fixtures (e.g., authentication tokens)
import pytest

from tests.utils import api_utils

@pytest.fixture
def citizen_token():
    return api_utils.get_auth_token("Citizen")

@pytest.fixture
def alt_citizen_token():
    return api_utils.get_auth_token("alternateCitizen")

@pytest.fixture
def architect_token():
    return api_utils.get_auth_token("citizenArchitect")

@pytest.fixture
def superuser_token():
    return api_utils.get_auth_token("Superuser")