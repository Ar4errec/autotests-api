from clients.api_client import APIClient
from httpx import Response
from pydantic import BaseModel
from clients.files.files_client import FileSchema
from clients.users.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.private_users_client import UserSchema


class CourseSchema(BaseModel):
    """
    Представляет схему для курса в образовательной системе.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema
    estimatedTime: str
    createdByUser: UserSchema


class CreateCourseResponseSchema(BaseModel):
    """
    Представляет схему ответа при создании курса.

    Этот класс предназначен для инкапсуляции данных ответа при создании
    курса. Он включает детали созданного курса, определённые в `CourseSchema`.

    :ivar course: Детали созданного курса.
    :type course: CourseSchema
    """
    course: CourseSchema

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса
    """
    userId: str


class CreateCourseRequestSchema(BaseModel):
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


class UpdateCoursesQuerySchema(BaseModel):
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
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод для получения курсов
        :param query: словарь с userId
        :return: Ответ от сервера в виде объекта Response
        """
        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получения курса по id
        :param course_id: id курса
        :return: Ответ от сервера в виде объекта Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCoursesQuerySchema) -> Response:
        """
        Метод для обновления курса
        :param course_id: id курса
        :param request: словарь с данными курса
        :return: Ответ от сервера в виде объекта Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаления курса
        :param course_id: id курса
        :return: Ответ от сервера в виде объекта Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
    Создаёт новый курс, вызывая API создания курса.

    Этот метод обрабатывает запрос на создание курса, используя предоставленные
    данные, инкапсулированные в `CreateCourseRequestSchema`. Он вызывает внешний
    эндпоинт API для выполнения создания и обрабатывает ответ API.
    Полученные данные затем валидируются и возвращаются в виде экземпляра
    `CreateCourseResponseSchema`.

    :param request: Входные данные для создания курса, представленные как экземпляр `CreateCourseRequestSchema`
    :type request: CreateCourseRequestSchema
    :return: Ответ от API создания курса, валидированный как экземпляр `CreateCourseResponseSchema`
    :rtype: CreateCourseResponseSchema
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PrivateUserscient.
    """
    return CoursesClient(client=get_private_http_client(user))