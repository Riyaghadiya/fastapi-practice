from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    status: str


class UserUpdate(BaseModel):
    name: str
    email: str
    phone: str
    status: str