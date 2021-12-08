from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# connection string format:  'postgresql://<user_name>:<password>@<ip or hostname>/<db_name>
SQL_ALCHEMY_DATABASE_URL =  'postgresql://postgres:anba@localhost/fastapi'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# FastAPI SQLAlchemy Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()