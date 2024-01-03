import json

def test_create_user(db_session,client):
    data={"username":"newtestuser","email":"newtest@example.com","password":"newtest"}
    response=client.post("/create-user",json=data)
    assert response.status_code==200
    response_data = response.json()
    assert response_data["username"] == data["username"]
    
    

#def test_delete_user_by_id(create_test_user,client):
    #user_id=create_test_user
    #response=client.delete(f"/user/{user_id}")
    #assert response.status_code==200
    #assert response.json()==f"User with ID {user_id} has been deleted."

#def test_update_user_by_id(create_test_user,client):
    #user_id=create_test_user
    #response=client.update("/user-update/{user_id}")
    #assert response.status_code==200
    #assert response.json()==f"User with ID {user_id} has been updated."


