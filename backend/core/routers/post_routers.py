from fastapi import APIRouter,Depends,UploadFile,Form,File,HTTPException
from sqlalchemy.orm import Session
from typing import Text
from schemas.posts import show_post
from core.crud.post_crud import create_new_post,update_post_by_id,delete_post_by_id,get_all_user_posts,update_post_image_by_id
from db.session import get_db
from core.routers.login_router import get_current_user
from db.models.users import User
from db.models.posts import Post


router=APIRouter()


@router.post("/post",response_model=show_post)
async def Create_new_post_router(owner_id:int,db:Session=Depends(get_db),image:UploadFile = File(None), 
                          caption: Text = Form(...)):
    try:
     new_post=await create_new_post(db=db,owner_id=owner_id,image=image,caption=caption)
     db.add(new_post)
     db.commit()
     db.refresh(new_post)
     return (new_post)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while creating the post.")
    



#update post router
@router.put("/update-post/{post_id}")
def update_post(post_id:int,post_new_data:dict,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    try:
     Postnew_data=update_post_by_id(post_id,post_new_data,db)
     if Postnew_data:
          return {"message":f"post with ID {post_id} has been updated"}
     else:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    except ValueError as e:
        print(f"A ValueError occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    


#update post image router
@router.put("/update-post-image/{post_id}")
def update_post_image(post_id:int,image:UploadFile=File(None),db:Session=Depends(get_db)):
    update_image=update_post_image_by_id(post_id=post_id,image=image,db=db)
    if update_image:
        return {"message":f"post image with ID {post_id} has been updated"}
     
    
        
  
# delete post router
@router.delete("/post/{post_id}")
def Deletepost(post_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
   
    try:
        Delete_post = delete_post_by_id(post_id, db, current_user)
        if Delete_post:
            return {"message": f"Post with ID {post_id} has been deleted"}
        else:
            raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    except ValueError as e:  # Catching a more specific exception
        print(f"A ValueError occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    


    # get all users posts router
@router.get("/all-user-posts/{owner_id}")
def Get_all_user_posts(owner_id:int,db=Session(get_db)):
     get_all_posts=get_all_posts(owner_id=owner_id,db=db)
     return get_all_posts
          
