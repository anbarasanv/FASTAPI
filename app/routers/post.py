from typing import List

from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from starlette.responses import Response


from .. import models
from ..database import get_db
from ..schema import Post, PostResponse
from ..oauth2 import get_current_user

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=List[PostResponse])
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=PostResponse)
async def get_posts(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=f"The post id: {id} did not found",
        )
    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
async def create_posts(
    post: Post,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The requested id: {id} content not found",
        )
    if post.first().owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"The requested id: {id} is not owned by you",
        )
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=PostResponse)
async def update_post(
    id: int,
    post: Post,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    post_data = db.query(models.Post).filter(models.Post.id == id)
    if not post_data.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"updating id: {id} not found"
        )
    if post_data.first().owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"The requested id: {id} is not owned by you",
        )
    post_data.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_data.first()
