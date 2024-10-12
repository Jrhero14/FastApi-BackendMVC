from starlette import status
from starlette.responses import JSONResponse

from app.services import UserService
from fastapi.encoders import jsonable_encoder


async def getUsersController():
    # Get User in with services
    users = UserService.getUsers()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "success",
            "message": "Success get all users",
            "data": jsonable_encoder(users),
        },
        headers={"Content-Type": "application/json"}
    )