from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import fake

class FileSchema(BaseModel):
    """
    Представляет схему и структуру файла.

    """
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Описание запроса на создание файла
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str  = Field(default="testData")
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Представляет схему ответа при создании файла.

    Этот класс используется для моделирования ответа, возвращаемого при успешном
    создании файла. Он инкапсулирует детали файла в форме объекта `FileSchema`.

    :ivar file: Детали созданного файла.
    :type file: FileSchema
    """
    file: FileSchema