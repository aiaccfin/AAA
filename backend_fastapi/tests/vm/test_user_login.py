import pytest

@pytest.mark.asyncio
def test_user_login_success(client):
    payload = {
        "email": "n2ew@example.com",
        "password": "123456"
    }
    response = client.post("/user/login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()

# @pytest.mark.asyncio
# async def test_user_login_fail(async_client):
#     payload = {
#         "email": "wrong_user",
#         "password": "wrong_pass"
#     }
#     response = await async_client.post("/user/login", json=payload)
#     assert response.status_code == 401
