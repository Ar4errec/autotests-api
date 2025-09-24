from pydantic import BaseModel, Field, EmailStr, constr
import uuid


class UserSchema(BaseModel):
    """
    Схема пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса создания пользователя
    """
    email: EmailStr
    password: str = Field(min_length=1, max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа создания пользователя
    """
    user: UserSchema
