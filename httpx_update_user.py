from venv import create

import httpx
from tools.fakers import get_random_email

create_payload = {
  "email": get_random_email(),
  "password": "123123",
  "lastName": "test",
  "firstName": "test",
  "middleName": "test"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_payload)
print("User create response:", create_user_response.json())
print("Status code:", create_user_response.status_code)


login_payload = {
  "email": create_user_response.json()["user"]["email"],
  "password": "123123"
}
# Логинимся
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("User Login response:", login_response_data)
print("Status code:", login_response.status_code)

# Достаём токен
access_token = login_response_data["token"]["accessToken"]
# Формируем заголовки
user_headers = {"Authorization": f"Bearer {access_token}"}

# Обновляем данные пользователя
user_id = create_user_response.json()["user"]["id"]

upgrade_user_payload = {
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", headers=user_headers, json=upgrade_user_payload)
print("User update response:", update_user_response.json())
print("Status code:", update_user_response.status_code)