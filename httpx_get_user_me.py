import httpx


login_payload = {
  "email": "test1@test.com",
  "password": "123123"
}
# Логинимся
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response:", login_response_data)
print("Status code:", login_response.status_code)


# Достаём токен
access_token = login_response_data["token"]["accessToken"]
# Формируем заголовки
user_me_headers = {"Authorization": f"Bearer {access_token}"}
user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=user_me_headers)
print("User response:", user_me_response.json())
print("Status code:", user_me_response.status_code)

