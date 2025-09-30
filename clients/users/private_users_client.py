from httpx import Response
from clients.api_client import APIClient
from pydantic import BaseModel
from clients.users.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema, UpdateUserResponseSchema, UserSchema


class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        """
        Метод получения информации по идентифекатору
        :param user_id: идентификатор пользователя
        :return: ответ сервера в виде объекта Response
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения информации по идентифекатору
        :param user_id: идентификатор пользователя
        :return: ответ сервера в виде объекта Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, requests: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления информации по идентифекатору
        :param user_id: Идентификатор пользователя
        :param requests: Словарь с данными для обновления
        :return: Ответ сервера в виде объекта Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=requests.model_dump(by_alias=True, exclude_unset=True))




    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору
        :param user_id: идентификатор пользователя
        :return: ответ сервера в виде объекта Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод получения информации по идентифекатору
        :param user_id:
        :return:
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))