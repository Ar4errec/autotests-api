from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    """
    Представляет схему для токенов, используемых в аутентификации.

    Этот класс определяет структуру для токенов доступа, типов токенов и
    токенов обновления, используемых в механизмах аутентификации. Использует
    BaseModel из pydantic для валидации и парсинга.

    :ivar access_token: Токен доступа, используемый для аутентификации.
    :type access_token: str
    :ivar token_type: Тип выданного токена (например, Bearer, JWT).
    :type token_type: str
    :ivar refresh_token: Токен, используемый для получения нового токена доступа.
    :type refresh_token: str
    """
    access_token: str = Field(alias="accessToken")
    token_type: str = Field(alias="tokenType")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class LoginResponseSchema(BaseModel):
    """
    Представляет схему ответа при входе в систему.

    Этот класс используется для определения структуры ответа, полученного
    при успешной операции входа. Он инкапсулирует соответствующие данные в
    структурированном формате для использования в приложении.

    :ivar token: Токен, возвращаемый при успешном входе.
    :type token: TokenSchema
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")  # Название ключа совпадает с API

