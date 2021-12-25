"""This the base module for the database
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from dotenv import load_dotenv
import os

from .config import settings

# load_dotenv()
# connection string format:  'postgresql://<user_name>:<password>@<ip or hostname>/<db_name>
# POSTGRES_DATABASE_URL = os.getenv("POSTGRES_DATABASE_URL")

POSTGRES_DATABASE_URL = settings.POSTGRES_DATABASE_URL

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
