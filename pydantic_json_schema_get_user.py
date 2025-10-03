from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.fakers import fake
from tools.assertion.schema import validate_json_schema



def test_get_user_pydantic_json_schema():
    # создаём клиентов
    public_users_client = get_public_users_client()
    private_users_client = get_private_users_client()

    # создаём пользователя
    create_user_request = CreateUserRequestSchema(
        email=fake.email(),
        password="string",
        last_name="string",
        first_name="string",
        middle_name="string"
    )
    create_user_response = public_users_client.create_user_api(create_user_request)
    created_user = create_user_response.json()

    # получаем пользователя по id
    get_user_response = private_users_client.get_user_api(created_user.id)
    get_user_json = get_user_response.json()

    # генерируем схему и валидируем
    validate_json_schema(
        instance=get_user_json,
        schema=GetUserResponseSchema.model_json_schema()
    )
