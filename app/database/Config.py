from typing import Generator
from typing import Any
import os


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.models import Base
from app.models.User import User

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

DB_CONNECTION=os.getenv('DB_CONNECTION')
DB_HOST=os.getenv('DB_HOST')
DB_USERNAME=os.getenv('DB_USERNAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_NAME=os.getenv('DB_NAME')
DB_PORT=os.getenv('DB_PORT')

connector = 'mysqlconnector' if (DB_CONNECTION == 'mysql') else 'null'

SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/testing"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, Any, None]:
    with SessionLocal() as session:
        yield session


async def create_tables():
    Base.metadata.create_all(bind=engine, checkfirst=True)

