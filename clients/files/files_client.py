from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.users.private_http_builder import get_private_http_client, AuthenticationUserDict


class File(TypedDict):
    id: str
    filename: str
    directory: str
    url: str


class CreateFileRequestDict(TypedDict):
    """
    Описание запроса на создание файла
    """
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseDict(TypedDict):
    file: File




class FilesClient(APIClient):
    """
    Класс для работы с /api/v1/files
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла по id файла
        :param file_id: Идентификатор файла
        :return: ответ сервера в виде Response
        """
        return self.get(f"/api/v1/files/{file_id}")



    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла
        :param request: Запрос на создание файла
        :return: ответ сервера в виде Response
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request["upload_file"], 'rb')}
        )


    def delete_files_api(self, file_id: str) -> Response:
         """
         Метод удаления файла по id файла
         :param file_id: Идентификатор файла
         :return: ответ сервера в виде Response
         """
         return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self,request: CreateFileRequestDict) -> CreateFileResponseDict:
        response = self. create_file_api(request)
        return response.json()



def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PrivateUserscient.
    """
    return FilesClient(client=get_private_http_client())