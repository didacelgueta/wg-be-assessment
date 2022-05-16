import pytest
from fastapi.testclient import TestClient

from wg_be_exam.app import create_app
from wg_be_exam.config import Config


@pytest.yield_fixture(scope="session")
def application():
    application = create_app(Config())
    return application


@pytest.yield_fixture(scope="session")
def test_client(application) -> None:
    with TestClient(application) as client:
        yield client
