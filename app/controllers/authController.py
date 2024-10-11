from starlette import status
from starlette.responses import JSONResponse

from app.dto import CreateUserDto
from app.dto.LoginUserDto import LoginUserDto
from app.services import UserService


async def registerUser(user: CreateUserDto) -> JSONResponse:

    # Process Register in UserService
    user = UserService.register(user)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "status": "success",
            "message": "User created successfully",
            "data": user.toJson()
        },
        headers={"Content-Type": "application/json"}
    )

async def login(body: LoginUserDto):

    token = UserService.login(body=body)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "status": "success",
            "message": "Login successfully",
            "token": token,
            "type": "bearer"
        },
        headers={"Content-Type": "application/json"}
    )