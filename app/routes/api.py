from app.controllers import authController
from app.services import UserService
from app.utilities import formating
from fastapi import APIRouter, status, HTTPException

from app.DTO.CreateUserDto import CreateUserDto
from app.DTO.GetUserDto import GetUserDto

router = APIRouter(
    prefix="/api",
    tags=["api"],
)

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=GetUserDto)
async def registerUser(bodyRequest: CreateUserDto):
    data = await authController.registerUser(user=bodyRequest)
    return data