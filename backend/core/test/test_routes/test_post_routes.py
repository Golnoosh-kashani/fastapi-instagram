import json
from io import BytesIO
#from db.models.posts import Post
#def test_create_post(db_session,create_test_user):
   # new_post = Post(owner_id=create_test_user, image="path/to/test/image.jpg", caption="Test Caption")
    ##db_session.add(new_post)
    #db_session.commit()
    #yield new_post.id
     # Optional teardown: delete the post after the test
    #db_session.delete(new_post)
    #db_session.commit()
    
def test_create_post(create_test_user,client):
    image_data=BytesIO(b"fake image data")
    image_data.name="test_image.jpg"
    data={"owner_id":create_test_user,"image":(image_data.name,image_data,"image/jpeg"),"caption":"Test caption"}
    response=client.post("/post",files=data)
    assert response.status_code == 200
    assert "caption" in response.json()
    assert response.json()["caption"] == "Test Caption"
    assert response.status_code==200

def test_update_post()    