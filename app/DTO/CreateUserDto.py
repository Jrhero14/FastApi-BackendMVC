from pydantic import BaseModel, Field


class CreateUserDto(BaseModel):
    name: str
    email: str
    password: str = Field(..., min_length=8)