from fastapi import APIRouter,Depends,UploadFile,Form,File
from sqlalchemy.orm import Session
from typing import Text
from schemas.posts import show_post
from core.crud.post_crud import create_new_post,update_post_by_id,delete_post_by_id,get_all_user_posts
from db.session import get_db
from db.models.posts import Post


router=APIRouter()


@router.post("/post",response_model=show_post)
async def Create_new_post_router(owner_id:int,db:Session=Depends(get_db),image:UploadFile = File(None), 
                          caption: Text = Form(...)):
    
    new_post=await create_new_post(db=db,owner_id=owner_id,image=image,caption=caption)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

@router.put("/update-post/{post_id}")
def update_post_by_id(post_id:int,post_new_data:dict,db:Session=Depends(get_db)):
    Postnew_data=update_post_by_id(post_id,post_new_data,db)
    if Postnew_data:
          return {"message":f"post with ID {post_id} has been updated"}
     

    
  
       
@router.delete("/post/{post_id}")
def Delete_post_by_id(post_id:int,db:Session=Depends(get_db)):
     Delete_post=delete_post_by_id(post_id,db)
     if Delete_post:
          return {"message":f"post with ID {post_id} has been updated"}

@router.get("/all-user-posts/{owner_id}")
def Get_all_user_posts(owner_id:int,db=Session(get_db)):
     get_all_posts=get_all_posts(owner_id=owner_id,db=db)
     return get_all_posts
          
