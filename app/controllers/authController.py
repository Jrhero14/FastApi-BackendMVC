from fastapi import HTTPException
from starlette import status

from app.DTO import CreateUserDto
from app.services import UserService
from app.utilities import formating


async def registerUser(user: CreateUserDto):
    email = formating.format_string(user.email)

    if not email:
        raise HTTPException(
            detail="Email can not be empty",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    if not user.password:
        raise HTTPException(
            detail="Password can not be empty",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    # Process Register in UserService
    user = UserService.register(user)

    return user