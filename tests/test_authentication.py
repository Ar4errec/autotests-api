from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertion.base import assert_status_code
from tools.assertion.authentication import assert_login_response
from tools.assertion.schema import validate_json_schema
from tools.fakers import fake


def test_login():
    """
    Проверяет процесс аутентификации:
    - создаёт нового пользователя,
    - выполняет login,
    - проверяет статус, схему и содержимое токенов.
    """


    public_client = get_public_users_client()
    authentication_client = get_authentication_client()


    email = fake.email()

    create_user_request = CreateUserRequestSchema(
        email=email,
        password="string",
        last_name="string",
        first_name="string",
        middle_name="string"
    )
    public_client.create_user(create_user_request)


    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    login_response = authentication_client.login_api(login_request)

    # Assert: проверяем статус ответа
    assert_status_code(login_response.status_code, HTTPStatus.OK)

    # Assert: валидируем тело ответа
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())

