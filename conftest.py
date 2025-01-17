from Nimbus.app import Nimbusapp
import pytest

@pytest.fixture
def app():
    return Nimbusapp()

@pytest.fixture
def test_client(app):
    return app.test_session()