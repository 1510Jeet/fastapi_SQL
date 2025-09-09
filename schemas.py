from typing import Optional
from pydantic import BaseModel, EmailStr

# Schema for the data inside the JWT token
class TokenData(BaseModel):
    email: Optional[EmailStr] = None

# Schema for the token response
class Token(BaseModel):
    access_token: str
    token_type: str

# Base user schema
class UserBase(BaseModel):
    name: str
    email: EmailStr
    nickname: Optional[str] = None

# Schema for creating a new user (includes password)
class UserCreate(UserBase):
    password: str

# Schema for reading/returning user data (excludes password)
class User(UserBase):
    id: int

    class Config:
        orm_mode = True
