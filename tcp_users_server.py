import socket

# Храним историю сообщений
messages = []

def server():
    # Создаём TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сервер к адресу и порту
    server_socket.bind(('localhost', 12345))

    # Сервер поддерживает до 10 одновременных подключений
    server_socket.listen(10)
    print("Сервер запущен и ждёт подключений на localhost:12345")

    while True:
        # Принимаем новое подключение
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        # Получаем сообщение от клиента
        data = client_socket.recv(1024).decode()
        if data:
            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

            # Добавляем сообщение в историю
            messages.append(data)

            # Отправляем клиенту всю историю сообщений
            history = '\n'.join(messages)
            client_socket.send(history.encode())

        # Закрываем соединение с клиентом
        client_socket.close()

if __name__ == "__main__":
    server()
