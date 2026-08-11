import pytest
from api.client import login
from config import USERNAME,PASSWORD
import logging

logging.basicConfig(level=logging.INFO)

@pytest.fixture
def authenticated():
    login(USERNAME, PASSWORD)

