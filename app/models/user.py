from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    #UserBase is a base model with common attributes.
    email: EmailStr

class UserCreate(UserBase):
    #UserCreate is used when creating a new user, including a password.
    password: str

class User(UserBase):
    #User is the main model representing a user, with an additional id and is_active field.
    id: int
    is_active: bool

    class Config:
        orm_mode =True

