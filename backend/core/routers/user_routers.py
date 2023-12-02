from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from schemas.users import user_input
from db.session import get_db
from db.models.users import User
from core.routers.login_router import get_current_user
from core.crud.user_crud import create_new_user,delete_user_by_id,update_user_by_id,get_all_users

router=APIRouter()

@router.post("/")
def CreateNewUser(user:user_input,db:Session=Depends(get_db)):
    add_user=create_new_user(user,db)
    return add_user


@router.delete("/user")
def DeleteUser(user_id:int,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    try:
          if current_user.id !=user_id:
               raise HTTPException(status_code=403, detail="Not authorized to perform this action")
          else:
           delete_user=delete_user_by_id(user_id,db)
          if delete_user:
              return {"message": f"User with ID {user_id} has been deleted."}
          else:
              raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found.")
    except Exception as e:
             raise HTTPException(status_code=500, detail="An error occurred while deleting the user.")


@router.put("/user-update/{user_id}")
def UpdateUser(user_id:int,new_user_data:dict,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
     if current_user.id !=user_id:
          raise HTTPException(status_code=403, detail="Not authorized to perform this action")
     else:
      Newuser_data=update_user_by_id(user_id,new_user_data,db)
     if Newuser_data:
          return {"message":f"user with ID {user_id} has been updated"}
     

@router.get("/all_users")
def Get_all_users(db:Session=Depends(get_db)):
     all_users=get_all_users(db)
     return all_users