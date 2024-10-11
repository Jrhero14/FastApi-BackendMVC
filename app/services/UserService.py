from fastapi import HTTPException
from starlette import status

from app.DTO import CreateUserDto
from app.models.User import User

from app.repositories import userRepository
from app.utilities.bcrypt_hashing import HashLib


def register(userDao: CreateUserDto) -> User:
    # Check Email Exist
    exist_user = userRepository.getByEmail(email=userDao.email)
    print(exist_user)
    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    # Hasing Password Process
    userDao.password = HashLib.hash(userDao.password)

    # Process Register with User Repository
    return userRepository.store(userDao.name, userDao.email, userDao.password)