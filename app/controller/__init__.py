from fastapi import APIRouter

from .users_controller import users_router
router= APIRouter()
router.include_router(users_router,prefix="/users")