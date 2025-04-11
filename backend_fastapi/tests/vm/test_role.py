def test_get_roles(client):
    response = client.get("/role")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
