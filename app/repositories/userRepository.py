from fastapi import HTTPException

from app.models.User import User
from database.config import SessionLocal


def store(name: str, email: str, password: str)-> User:
    userReturn = User()
    userReturn.name = name
    userReturn.email = email
    userReturn.password = password

    try:
        with SessionLocal.begin() as session:
            user = User()
            user.name = name
            user.email = email
            user.password = password

            session.add(user)
            session.flush()

            userReturn.id = user.id
            userReturn.created_at = user.created_at
            userReturn.updated_at = user.updated_at
        return userReturn
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e))

def getbyid(id: int) -> User:
    with SessionLocal() as session:
        return session.query(User).filter(User.id == id).first()

def getByEmail(email: str):
    with SessionLocal() as session:
        return session.query(User).where(User.email == email).first()


def getUsers():
    with SessionLocal() as session:
        return session.query(User).all()