from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict



class UpdateUserRequestDict(TypedDict):
    email: str | None = None
    lastName: str | None = None
    firstName: str | None = None
    middleName: str | None = None



class PrivateUsersClient(APIClient):
    def get_get_user_me_api(self) -> Response:
        """
        Метод получения информации по идентифекатору
        :param user_id: идентификатор пользователя
        :return: ответ сервера в виде объекта Response
        """
        return self.get("/api/v1/users/me")

    def get_get_user_api(self, user_id: str) -> Response:
        """
        Метод получения информации по идентифекатору
        :param user_id: идентификатор пользователя
        :return: ответ сервера в виде объекта Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, requests) -> Response:
        """
        Метод обновления информации по идентифекатору
        :param user_id: Идентификатор пользователя
        :param requests: Словарь с данными для обновления
        :return: Ответ сервера в виде объекта Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=requests)




    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору
        :param user_id: идентификатор пользователя
        :return: ответ сервера в виде объекта Response
        """
        return self.delete(f"/api/v1/users/{user_id}")


