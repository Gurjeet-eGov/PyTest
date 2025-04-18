import pytest
import json

ENV_PATH = "config/env_config.json"
CRED_PATH = "config/credentials.json"
ENDPOINT_PATH = "config/endpoints.json"
CREDS_ENV_KEY = "credentials"

@pytest.fixture(scope="session", autouse=True)
def get_env_data():
    """Load environment configuration data."""
    with open(ENV_PATH) as f:
        env_config = json.load(f)
    return env_config

@pytest.fixture(scope="session", autouse=True)
def get_credentials():
    """Load credentials data."""
    with open(ENV_PATH) as f:
        creds = json.load(f)
    return creds[CREDS_ENV_KEY]

@pytest.fixture(scope="session", autouse=True)
def get_endpoints():
    """Load endpoints data."""
    with open(ENDPOINT_PATH) as f:
        endpoints = json.load(f)
    return endpoints
