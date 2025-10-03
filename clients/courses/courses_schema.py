from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Схема курса для GET-запросов.
    """
    id: str
    title: str
    maxScore: int = Field(alias="maxScore")
    minScore: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseResponseSchema(BaseModel):
    """
    Схема ответа при создании курса
    """
    course: CourseSchema



class GetCoursesQuerySchema(BaseModel):
    userId: str


class CreateCourseRequestSchema(BaseModel):
    """
    Схема запроса для создания курса
    """
    title: str = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)  # только ID пользователя для POST


class UpdateCoursesQuerySchema(BaseModel):
    """
    Схема запроса для обновления курса
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
