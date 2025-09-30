from pydantic import BaseModel, HttpUrl


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
    filename: str
    directory: str
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