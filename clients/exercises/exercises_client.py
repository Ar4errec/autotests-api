from pydantic import BaseModel
from httpx import Response
from clients.api_client import APIClient
from clients.users.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений
    """
    courseId: str


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка упражнений
    """
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании упражнения
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа при обновлении упражнения
    """
    exercise: ExerciseSchema


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Отправляет запрос GET /api/v1/exercises
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Отправляет запрос GET /api/v1/exercises/{exercise_id}
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Отправляет запрос POST /api/v1/exercises
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Отправляет запрос PATCH /api/v1/exercises/{exercise_id}
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Отправляет запрос DELETE /api/v1/exercises/{exercise_id}
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # Методы с возвратом JSON

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получает список упражнений
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> ExerciseSchema:
        """
        Получает одно упражнение по id
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создаёт упражнение
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Обновляет данные упражнения
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    def delete_exercise(self, exercise_id: str) -> None:
        """
        Удаляет упражнение
        """
        self.delete_exercise_api(exercise_id)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Создаёт экземпляр ExercisesClient с авторизованным HTTP-клиентом
    """
    return ExercisesClient(client=get_private_http_client(user))
