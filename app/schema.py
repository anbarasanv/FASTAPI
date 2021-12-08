from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pydantic.networks import EmailStr

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class PostResponse(Post):
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    accss_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None

