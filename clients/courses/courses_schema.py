from pydantic import BaseModel, Field
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema



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
    title: str
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")  # только ID пользователя для POST


class UpdateCoursesQuerySchema(BaseModel):
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
