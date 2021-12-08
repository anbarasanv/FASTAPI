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

# @app.get('/posts', response_model= List[PostResponse])
# async def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return posts

# @app.get('/posts/{id}', status_code=status.HTTP_200_OK, response_model= PostResponse)
# async def get_posts(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
#                             detail=f"The post id: {id} did not found")
#     return post

# @app.post('/createposts', status_code=status.HTTP_201_CREATED, response_model= PostResponse)
# async def create_posts(post: Post, db: Session = Depends(get_db)):
#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)

#     return new_post

# @app.delete('/deleteposts/{id}', status_code=status.HTTP_204_NO_CONTENT)
# async def delete_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id)
#     ret_data = post.first()
#     if not post.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The requested id: {id} content not found")
#     post.delete(synchronize_session=False)
#     db.commit()
#     db.refresh(ret_data)
#     return ret_data

# @app.put('/posts/{id}', status_code=status.HTTP_200_OK, response_model= PostResponse)
# async def update_post(id: int, post: Post, db: Session = Depends(get_db)):
#     post_data = db.query(models.Post).filter(models.Post.id == id)
#     ret_data = post_data.first()
#     if not post_data.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"updating id: {id} not found")
#     post_data.update(post.dict(), synchronize_session=False)
#     db.commit()
#     db.refresh(ret_data)
#     return ret_data

# #################################################
# #  API's For Users Schema                       #
# #################################################
# @app.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):

#     user.password = utility.hash(user.password)
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/users/{id}', status_code=status.HTTP_200_OK, response_model=UserResponse)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id: {id} does not exists')
#     return user
