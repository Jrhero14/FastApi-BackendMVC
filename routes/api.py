from typing import Annotated

from starlette.responses import JSONResponse

from app.controllers import authController
from fastapi import APIRouter, status, Depends

from app.dto.CreateUserDto import CreateUserDto
from app.dto.LoginUserDto import LoginUserDto
from utilities.jwtUtils import validate_token

router = APIRouter(
    prefix="/api",
    tags=["Authentication"],
)

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/register", status_code=status.HTTP_201_CREATED, response_class=JSONResponse)
async def registerUser(bodyRequest: CreateUserDto):
    response = await authController.registerUser(user=bodyRequest)
    return response

@router.post("/login", status_code=status.HTTP_200_OK, response_class=JSONResponse)
async def login(bodyRequest: LoginUserDto):
    response = await authController.login(body=bodyRequest)
    return response

@router.post("/validate-token", status_code=status.HTTP_200_OK, response_class=JSONResponse, dependencies=[Depends(validate_token)])
async def login():
    return {
        "message": "Token valid"
    }