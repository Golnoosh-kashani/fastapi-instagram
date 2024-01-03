import json
from io import BytesIO
from db.models.posts import Post

def test_create_post(log_in_test_user,client):
    token = log_in_test_user

    headers = {'Authorization': f'Bearer {token}'}

    image_data = BytesIO(b"fake image data")
    image_data.name = "test_image.jpg"
    data = {
        "caption": "Test Caption"
    }
    files = {
        "image": (image_data.name, image_data, "image/jpeg")
    }

    response = client.post("/post", headers=headers, data=data, files=files)
    print(response.json())

    assert response.status_code == 200
def test_update_post(test_post_id,client,create_test_user, log_in_test_user):
    token = log_in_test_user
    headers = {'Authorization': f'Bearer {token}'}
    
    new_data = {"caption": "Updated caption"}
    response = client.put(f"/posts/{test_post_id}", json=new_data, headers=headers)
    print (response.json())


    assert response.status_code == 200
    assert response.json() == {"message": f"post with ID {test_post_id} has been updated"}



def test_delete_post(test_post_id,client,create_test_user, log_in_test_user):
    token = log_in_test_user
    headers = {'Authorization': f'Bearer {token}'}
    
    response = client.delete(f"/posts/{test_post_id}",  headers=headers)
    print (response.json())


    assert response.status_code == 200
    assert response.json() == {"message": f"post with ID {test_post_id} has been updated"}
    