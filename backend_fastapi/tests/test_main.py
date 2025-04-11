import pytest

@pytest.mark.asyncio
async def test_root(async_client):
    response = await async_client.get("/test")
    assert response.status_code == 200
    assert "xAIBooks" in response.json()
