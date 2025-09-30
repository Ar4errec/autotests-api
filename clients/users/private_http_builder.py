from httpx import Client
from pydantic import BaseModel, Field
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    """
    Объект для аутентификации пользователя
    """
    email: str
    password: str


# Если JSON от API возвращает accessToken, используем alias
class TokenSchema(BaseModel):
    """
    Представляет схему для аутентификационных токенов.

    Этот класс используется для определения структуры ответа с аутентификационным токеном.
    Он задаёт необходимые поля данных и обеспечивает строгие правила именования с помощью alias.

    :ivar access_token: Токен, выдаваемый после успешной аутентификации,
    часто используется для авторизации доступа к защищённым ресурсам.
    :type access_token: str

    """
    access_token: str = Field(alias="accessToken")


class LoginResponseSchema(BaseModel):
    """
    Представляет структуру ответа при входе в систему.

    Этот класс используется для моделирования структуры данных ответа, получаемого
    после успешного входа. Он содержит информацию, такую как данные токена,
    которые инкапсулированы в `TokenSchema`.

    :ivar token: Данные токена, связанные с ответом на вход в систему.
    :type token: TokenSchema
    """
    token: TokenSchema


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.
    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию httpx.Client с установленным заголовком Authorization.
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    # Теперь обращаемся к access_token, а не к accessToken
    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
