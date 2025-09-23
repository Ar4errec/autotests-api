"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}"""
import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic .alias_generators import to_camel

class FileShema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class UserShema(BaseModel):
    id: str
    email: EmailStr
    lastName: str = Field(alias="lastName")
    firstName: str = Field(alias="firstName")
    middleName: str = Field(alias="middleName")

    @computed_field
    def username(self) -> str:
        return f"{self.firstName} {self.lastName}"

    def get_username(self):
        return f"{self.firstName} {self.lastName}"


class CourseSchema(BaseModel):
    # model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Python"
    max_score: int = Field(alias="maxScore", default=100)
    min_score: int = Field(alias="minScore", default=10)
    description: str = "Python API course"
    preview_file: FileShema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="1 weeks")
    created_by_user: UserShema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id="course-id",
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    previewFile=FileShema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses"
    ),
    estimatedTime="1 weeks",
    createdByUser=UserShema(
        id="user-id",
        email="alice@test.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice"
    ))

print(course_default_model)

course_dict = {
    "id": "course-id",
    "title": "Python",
    "maxScore": 100,
    "minScore": 10,
    "description": "Python API course",
    "previewFile": {
        "id":"file-id",
        "url":"http://localhost:8000",
        "filename":"file.png",
        "directory":"courses"
    },
    "estimatedTime": "1 weeks",
    "createdByUser":{
        "id": "user-id",
        "email": "alice@test.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
}



course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
print(course_dict_model.model_dump())
print(course_dict_model.model_dump(by_alias=True))

course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))

try:
    user = UserShema(
        id="user-id",
        email="ba@ba.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice"
    )
except ValidationError as error:
    print(error)
    print(error.errors())

