from os import access
from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models
from .. import database, schema, utility, oauth2


router = APIRouter(tags=["Authentication"])

@router.post('/login')
def login(user_cred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_cred.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid credentials name')
    if not utility.verify(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials pwd')

    access_token = oauth2.get_accesss_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type":"bearer"}