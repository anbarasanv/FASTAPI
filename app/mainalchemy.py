from fastapi import FastAPI, status, HTTPException, Depends
from passlib.utils.decor import deprecated_function
from sqlalchemy.orm import Session
from typing import List
from . import models
from .database import engine, get_db
from .schema import Post, PostResponse, UserCreate, UserResponse
from . import utility
from .routers import user, post, auth

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)