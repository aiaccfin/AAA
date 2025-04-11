import pytest
import pytest_asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient

from app.main import create_app
from app.config import test_settings
from app.utils import u_auth_py


@pytest.fixture(scope="session")
def app():
    return create_app(test_settings)


@pytest_asyncio.fixture
async def async_client(app, monkeypatch):
    # Mock authent to bypass auth dependency
    def fake_auth(_):
        return "mock_user"

    monkeypatch.setattr(u_auth_py, "authent", fake_auth)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def client(app, monkeypatch):
    # Mock authent to bypass auth dependency
    def fake_auth(_):
        return "mock_user"

    monkeypatch.setattr(u_auth_py, "authent", fake_auth)

    return TestClient(app)
