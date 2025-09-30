from httpx import Response
from clients.api_client import APIClient
from clients.users.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
    GetExerciseQuerySchema,
    GetExerciseResponseSchema,
    ExerciseSchema
)


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExerciseQuerySchema) -> Response:
        """
        Отправляет запрос GET /api/v1/exercises с query-параметрами
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

    # Методы с возвратом Pydantic-моделей

    def get_exercises(self, query: GetExerciseQuerySchema) -> GetExerciseResponseSchema:
        """
        Получает список упражнений
        """
        response = self.get_exercises_api(query)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Получает одно упражнение по id
        """
        response = self.get_exercise_api(exercise_id)
        # Валидируем через Pydantic
        return GetExerciseResponseSchema.model_validate_json(response.text())

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создаёт новое упражнение
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
