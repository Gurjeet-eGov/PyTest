import pytest
import json

@pytest.fixture(scope="session", autouse=True)
def get_env_data():
    """Load environment configuration data."""
    with open("tests/config/env_config.json") as f:
        env_config = json.load(f)
    return env_config

@pytest.fixture(scope="session", autouse=True)
def get_credentials():
    """Load environment configuration data."""
    with open("tests/config/credentials.json") as f:
        creds = json.load(f)
    return creds

@pytest.fixture(scope="session", autouse=True)
def get_endpoints():
    """Load environment configuration data."""
    with open("tests/config/endpoints.json") as f:
        endpoints = json.load(f)
    return endpoints
