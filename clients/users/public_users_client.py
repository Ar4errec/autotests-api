from typing import TypedDict
from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


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
