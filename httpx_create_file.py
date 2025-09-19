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


create_files_headers = {
    "Authorization": f"Bearer {access_token}"
}

create_files_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    headers = create_files_headers,
    data = {"filename": "test.png", "directory": "test"},
    files = {"upload_file": open('./testData/files/test.png', 'rb')}
)

create_file_response_data = create_files_response.json()
print(create_files_response.status_code)
print("File create response:", create_file_response_data)



