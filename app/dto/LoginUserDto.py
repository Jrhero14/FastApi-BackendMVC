from pydantic import BaseModel, EmailStr

class LoginUserDto(BaseModel):
    email: EmailStr
    password: str

