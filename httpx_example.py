import httpx
#
# base_url = "https://jsonplaceholder.typicode.com/todos/"
# data = {
#     "userId": 21,
#     "title": "testos tustos",
#     "completed": False
#   }
#
# response = httpx.post(base_url, json=data)
#
#
# print(response.json())
# print(response.status_code)
#
#
# data = {'user_name': 'test', 'password': 'testtest'}
# headers = {"Authorization": "Bearer my_secret_token"}
#
# response = httpx.post("https://httpbin.org/post", headers=headers, json=data)
# print(response.json())
# print(response.status_code)
#
#
# files = {'file':("example.txt", open('example.txt', 'rb'))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.json())


# with httpx.Client() as client:
#     response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
#     response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
#
# print(response1.json())
# print(response2.json())
#
#
# client = httpx.Client(headers={'Content-Type': 'application/json'})
# response = client.get('https://httpbin.org/get')
# print(response.json())
try:
    response = httpx.get('https://jsonplaceholder.typicode.com/todos/invalid')
    response.raise_for_status()
    print(response.status_code)
except httpx.HTTPError as e:
    print(f"Ошибка запроса: {e}")


try:
    response = httpx.get(url: "https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
        print("Запрос превысил лимит времени"))