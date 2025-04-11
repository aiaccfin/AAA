import uuid

def test_create_group(client):
    group_name = f"Test Group {uuid.uuid4()}"
    payload = {
        "name": "Test Group",
        "description": "Test description",
        "biz_entities": ["entity_001", "entity_002"]
    }
    response = client.post("/group", json=payload)
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "Test Group"
    assert data["biz_entities"] == ["entity_001", "entity_002"]
