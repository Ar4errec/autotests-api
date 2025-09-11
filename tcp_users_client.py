import socket

def client():
    # Создаём TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключаемся к серверу
    client_socket.connect(('localhost', 12345))

    # Отправляем сообщение серверу
    message = "Привет, сервер!"
    client_socket.send(message.encode())

    # Получаем историю сообщений от сервера
    response = client_socket.recv(1024).decode()
    print(response)

    # Закрываем соединение
    client_socket.close()

if __name__ == "__main__":
    client()
