from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertion.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что данные созданного пользователя в ответе совпадают с данными запроса.

    :param request: Объект запроса CreateUserRequestSchema с исходными данными пользователя.
    :param response: Объект ответа CreateUserResponseSchema с данными созданного пользователя.
    :raises AssertionError: Если значения email, last_name, first_name или middle_name не совпадают.
    """
    assert_equal(response.user.email, request.email, name="email")
    assert_equal(response.user.last_name, request.last_name, name="last_name")
    assert_equal(response.user.first_name, request.first_name, name="first_name")
    assert_equal(response.user.middle_name, request.middle_name, name="middle_name")






