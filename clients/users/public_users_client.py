from httpx import Response
from pydantic import BaseModel, Field

from clients.api_client import APIClient
from clients.public_httpx_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами /api/v1/users.
    Включает эндпоинты, которые не требуют авторизации (например, создание пользователя).
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
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
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Создаёт нового пользователя в системе.

        :param request: Словарь с данными пользователя.
            Обязательные поля:
                - email: str — адрес электронной почты пользователя
        :param request:
        :return:
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр класса PublicUsersClient с использованием публичного http-клиента.
    :return: Готовый к использованию экземпляр httpx.Client.
    """
    return PublicUsersClient(client=get_public_http_client())
