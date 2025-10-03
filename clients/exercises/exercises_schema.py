from pydantic import BaseModel, Field
from tools.fakers import fake


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



class GetExerciseQuerySchema(BaseModel):
    """
    Схема запроса на получение списка упражнений
    """
    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Схема запроса на создание упражнения
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    """
    Схема запроса на обновление упражнения
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)




class GetExerciseResponseSchema(BaseModel):
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

