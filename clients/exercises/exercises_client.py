from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.users.private_http_builder import get_private_http_client, AuthenticationUserDict


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса
    """
    courseId: str

class CreateExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса для создания курса
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExercisesCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса для обновления курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Класс для работы с упражнениями /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения списка упражнений по курсу
        :param query: Словарь с courseId
        :return: Ответ от сервера в виде httpx Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получения информации об упражнении по id
        :param exercise_id: id упражнения
        :return: Ответ от сервера в виде httpx Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, exercise_id: str, request: CreateExercisesQueryDict) -> Response:
        """
        Метод для создания упражнения
        :param request: Словарь с параметрами упраженения
        :return: Ответ от сервера в виде httpx Response
        """
        return self.post(f"/api/v1/exercises/{exercise_id}", json=request)

    def update_exercises_api(self, exercise_id: str, request: UpdateExercisesCoursesQueryDict) -> Response:
        """
        Метод для обновления упражнения
        :param request: Словарь с параметрами курса
        :return: Ответ от сервера в виде httpx Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения
        :param exercise_id: id упражнения
        :return: Ответ от сервера в виде httpx Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

def get_courses_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PrivateUserscient.
    """
    return ExercisesClient(client=get_private_http_client())