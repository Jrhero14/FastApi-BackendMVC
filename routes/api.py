from starlette.responses import JSONResponse

from app.controllers import authController, userController
from fastapi import APIRouter, status, Depends

from app.dto.CreateUserDto import CreateUserDto
from app.dto.LoginUserDto import LoginUserDto
from utilities.jwtUtils import validate_token, refreshJwtToken

router = APIRouter(
    prefix="/api",
    tags=["Authentication"],
)

@router.get("/")
async def root():
    return {"message": "Hello World"}

# Auth Controllers
@router.post("/register", status_code=status.HTTP_201_CREATED, response_class=JSONResponse)
async def registerRoute(bodyRequest: CreateUserDto):
    response = await authController.registerUserController(user=bodyRequest)
    return response

@router.post("/login", status_code=status.HTTP_200_OK, response_class=JSONResponse)
async def loginRoute(bodyRequest: LoginUserDto):
    response = await authController.loginController(body=bodyRequest)
    return response

@router.post("/validate-token", status_code=status.HTTP_200_OK, response_class=JSONResponse, dependencies=[Depends(validate_token)])
async def loginRoute():
    return {
        "message": "Token valid"
    }

@router.post("/refresh-token", status_code=status.HTTP_200_OK, response_class=JSONResponse, dependencies=[Depends(refreshJwtToken)])
async def refreshRoute():
    pass

# Users Controllers
@router.get("/get-users", status_code=status.HTTP_200_OK, response_class=JSONResponse, dependencies=[Depends(validate_token)], tags=["Users"])
async def getUsersRoute():
    response = await userController.getUsersController()
    return response