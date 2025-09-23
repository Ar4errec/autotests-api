from typing import TypedDict
from httpx import Response

from clients.api_client import APIClient
from clients.public_httpx_builder import get_public_http_client


class User(TypedDict):
    """
    Описывает структуру данных пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    MiddleName: str

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """
    Описывает структуру ответа сервера при создании пользователя.
    """
    user: User


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами /api/v1/users.
    Включает эндпоинты, которые не требуют авторизации (например, создание пользователя).
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создаёт нового пользователя в системе.

        :param request: Словарь с данными пользователя.
            Обязательные поля:
                - email: str — адрес электронной почты пользователя
                - password: str — пароль пользователя
                - lastName: str — фамилия
                - firstName: str — имя
                - middleName: str — отчество
        :return: Объект httpx.Response с данными ответа сервера.
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        """
        Создаёт нового пользователя в системе.

        :param request: Словарь с данными пользователя.
            Обязательные поля:
                - email: str — адрес электронной почты пользователя
        :param request:
        :return:
        """
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр класса PublicUsersClient с использованием публичного http-клиента.
    :return: Готовый к использованию экземпляр httpx.Client.
    """
    return PublicUsersClient(client=get_public_http_client())
