from pydantic import BaseModel, Field



class ExerciseSchema(BaseModel):
    """
    Схема упражнения для GET-запросов.
    """
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")



class GetExercisesQuerySchema(BaseModel):
    """
    Схема запроса на получение списка упражнений
    """
    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Схема запроса на создание упражнения
    """
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
    Схема запроса на обновление упражнения
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")



class GetExercisesResponseSchema(BaseModel):
    """
    Схема ответа на получение списка упражнений
    """
    exercises: list[ExerciseSchema]


class CreateExerciseResponseSchema(BaseModel):
    """
    Схема ответа при создании упражнения
    """
    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """
    Схема ответа при обновлении упражнения
    """
    exercise: ExerciseSchema
