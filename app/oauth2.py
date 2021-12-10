from jose import jwt, JWTError
from datetime import datetime, timedelta

from sqlalchemy.orm.session import Session
from app import models

from app.database import get_db
from . import schema
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')


def get_accesss_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({'exp': expire})

    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return jwt_token


def verify_accesss_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get('user_id')

        if id is None:
            raise credential_exception
        token_data = schema.TokenData(id=id)
    except JWTError:
        raise credential_exception
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'})
    token = verify_accesss_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user
