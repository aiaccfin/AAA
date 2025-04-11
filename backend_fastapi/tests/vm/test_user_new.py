import uuid

def test_user_register_success(client):
    random_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    payload = {
        "email": random_email,
        "name": "new_user",  
        "password_hash": "123456",
        "roles": ["role_001"],
        "groups": ["group_001"],
        "primary_role": "role_001",
        "primary_group": "group_001",
        "email_verified": False,
        "is_verified": False
    }

    response = client.post("/user/register", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "new_user"
