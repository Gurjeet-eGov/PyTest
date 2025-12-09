import pytest
import json

from utils import api_utils

ENV_PATH = "config/env_config.json"
CRED_PATH = "config/credentials.json"
ENDPOINT_PATH = "config/endpoints.json"

@pytest.fixture(scope="session", autouse=True)
def get_env_data():
    """Load environment configuration data."""
    with open(ENV_PATH) as f:
        env_config = json.load(f)
    return env_config

@pytest.fixture(scope="session", autouse=True)
def get_credentials():
    """Load credentials data."""
    with open(CRED_PATH) as f:
        creds = json.load(f)
    return creds

@pytest.fixture(scope="session", autouse=True)
def get_endpoints():
    """Load endpoints data."""
    with open(ENDPOINT_PATH) as f:
        endpoints = json.load(f)
    return endpoints

@pytest.fixture(scope="module")
def get_reqInfo():
    tokens = {
        "Superuser": api_utils.get_reqInfo("Superuser"),
        # "Architect": api_utils.get_reqInfo("citizenArchitect"),
        # "Citizen": api_utils.get_reqInfo("Citizen"),
        # "AltCitizen": api_utils.get_reqInfo("alternateCitizen")
    }
    return tokens
