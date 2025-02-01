from fastapi import APIRouter, Request
from pydantic import BaseModel, constr
import re
from database.userservice import *

users_router = APIRouter(tags=["Управление юзерами"],
                         prefix="/user")

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    return False
class User(BaseModel):
    user_name: str
    phone_number: str
    email: str
    password: constr(min_length=5, max_length=10)
    birthday: str | None = None
    city: str | None = None
@users_router.post("/registration")
async def register_user(user_model: User):
    data = dict(user_model)
    mail_validator = mail_checker(user_model.email)
    if mail_validator:
        result = registration_db(**data)
        return {"status": 1, "message" : result}
    return {"status": 0, "message": "неправильная формат email"}

@users_router.post("/login")
async def login_user(request: Request):
    data = await request.json()
    result = login_db(identificator=data.get("identificator"),
                      password=data.get("password"))
    return {"status": 1, "message": result}