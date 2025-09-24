from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """
    Схема пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса создания пользователя
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа создания пользователя
    """
    user: UserSchema
