from fastapi import APIRouter
from core.routers.user_routers import router as user_routers
from core.routers.post_routers import router as post_routers
from core.routers.login_router import router as login_router
from core.routers.comment_router import router as comment_router


api_router=APIRouter()


api_router.include_router(user_routers)
api_router.include_router(post_routers)
api_router.include_router(login_router)
api_router.include_router(comment_router)
