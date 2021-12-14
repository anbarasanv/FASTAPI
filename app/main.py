"""This the main package for the application
"""
from fastapi import FastAPI
from fastapi.params import Depends
from . import models
from .database import engine
from .routers import user, post, auth

# This line creates the required database tables,if not exists already
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
