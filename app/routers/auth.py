from os import access
from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models
from .. import database, utility, oauth2, schema


router = APIRouter(tags=["Authentication"])

@router.post('/login', response_model=schema.Token, status_code=status.HTTP_200_OK)
def login(user_cred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_cred.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect username or password")
    if not utility.verify(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect username or password")

    access_token = oauth2.get_accesss_token(data={"user_id": user.id})

    return {"access_token": str(access_token), "token_type": "bearer"}