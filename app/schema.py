"""This module contains the validation schemas for the API.
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pydantic.networks import EmailStr
from pydantic.types import conint


class UserCreate(BaseModel):
    """this class defines the schema for the UserCreate model.

    Args:
        BaseModel (pydantic BaseModel): This is the base model for the UserCreate model.
    """

    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """this class defines the schema for the UserResponse model.

    Args:
        BaseModel (pydantic BaseModel): This is the base model for the UserResponse model.
    """

    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    """this class defines the schema for the UserLogin model.

    Args:
        BaseModel (pydantic BaseModel): This is the base model for the UserLogin model.
    """

    email: EmailStr
    password: str


class Post(BaseModel):
    """This class defines the schema for the Post model.

    Args:
        BaseModel (pydantic BaseModel): The base model for the Post model.
    """

    title: str
    content: str
    published: bool = True


class PostResponse(Post):
    """this class defines the schema for the PostResponse model.

    Args:
        Post (pydantic BaseModel): The base model for the PostResponse model.
    """

    id: int
    created_at: datetime
    owner: UserResponse

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    """this class defines the schema for the PosOut model.

    Args:
        Post (pydantic BaseModel): The base model for the PosOut model.
    """

    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    """this class defines the schema for the Token model.

    Args:
        BaseModel (pydantic BaseModel): This is the base model for the Token model.
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """this class defines the schema for the TokenData model.
    Args:
        BaseModel (pydantic BaseModel): The base model for the Post model.
    """

    id: Optional[str] = None


class Vote(BaseModel):
    """this class defines the schema for the Vote model.

    Args:
        BaseModel (pydantic BaseModel): The base model for the Vote model.
    """

    post_id: int
    direction: conint(ge=0, le=1)
