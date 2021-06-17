import pytest
from app_core import app_main


@pytest.fixture
def app():
    return app_main.app
