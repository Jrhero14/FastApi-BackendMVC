from datetime import timedelta

from fastapi import HTTPException
from starlette import status

from app.dto import CreateUserDto
from app.dto.LoginUserDto import LoginUserDto
from app.models.User import User

from app.repositories import userRepository
from utilities.bcrypt_hashing import HashingUtils
from utilities.jwtUtils import create_access_token

from utilities.jwtUtils import ACCESS_TOKEN_EXPIRE_MINUTES


def register(userDao: CreateUserDto) -> User:
    # Check Email Exist
    exist_user = userRepository.getByEmail(email=userDao.email)
    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Email already exist"
        )

    # Hasing Password Process
    userDao.password = HashingUtils.hash(userDao.password)

    # Process Register with User Repository
    return userRepository.store(userDao.name, userDao.email, userDao.password)

def login(body: LoginUserDto):
    # Get User with email
    user = userRepository.getByEmail(email=body.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Email not found"
        )

    # Validate Login
    valid = HashingUtils.validate(plain_password=body.password, hashed_password=user.password)
    if not valid:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid Password"
        )

    # Generate JWT Token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(payload={"user_id": user.id}, expires_delta=access_token_expires)

    return token
