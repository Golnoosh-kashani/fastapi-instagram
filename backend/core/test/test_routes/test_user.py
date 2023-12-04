import json

def test_create_user(client):
    data={"username":"testuser","email":"test@example.com","password":"test"}
    response=client.post("/",json.dumps(data))
    assert response.status_code==200
    assert response.json()["email"]=="test@example.com"
    user_id = response.json()["id"]
    return user_id

def test_delete_user_by_id(create_test_user,client):
    user_id=create_test_user
    response=client.delete(f"/user/{user_id}")
    assert response.status_code==200
    assert response.json()==f"User with ID {user_id} has been deleted."

def test_update_user_by_id(create_test_user,client):
    user_id=create_test_user
    response=client.update("/user-update/{user_id}")
    assert response.status_code==200
    assert response.json()==f"User with ID {user_id} has been updated."


