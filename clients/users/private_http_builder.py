from multiprocessing.connection import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict
from typing import TypedDict



class AuthenticationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    функция создаёт экземпляр httpx.Client c аутентификацией пользователя.
    :param user: Объект AuthenticationUserSchema c email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    :param user:
    :return:
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )

