from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса
    """
    userId: str


class CreateCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса для создания курса
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса для обновления курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    Класс для работы с курсами /api/v1/courses
    """
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод для получения курсов
        :param query: словарь с userId
        :return: Ответ от сервера в виде объекта Response
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получения курса по id
        :param course_id: id курса
        :return: Ответ от сервера в виде объекта Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCoursesQueryDict) -> Response:
        """
        Метод для создания курса
        :param request: словарь с данными курса
        :return: Ответ от сервера в виде объекта Response
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCoursesQueryDict) -> Response:
        """
        Метод для обновления курса
        :param course_id: id курса
        :param request: словарь с данными курса
        :return: Ответ от сервера в виде объекта Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаления курса
        :param course_id: id курса
        :return: Ответ от сервера в виде объекта Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")
