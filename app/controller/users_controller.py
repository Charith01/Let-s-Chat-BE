from fastapi import APIRouter
from app.service.users_service import UsersService

users_router = APIRouter(tags=['users'])

@users_router.get("/get-users")
def get_users():
    print("enter get_users controller")
    service_obj=UsersService()
    resp=service_obj.get_users()
    return resp

@users_router.post("/create-user")
def create_user(input:dict):
    print("enter create_user controller")
    service_obj = UsersService()
    resp = service_obj.create_user(input)
    return resp

@users_router.post("/validate-user")
def validate_user(input:dict):
    print("enter validate_user controller")
    service_obj=UsersService()
    resp=service_obj.validate_user(input)
    return resp