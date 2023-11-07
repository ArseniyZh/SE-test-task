import socket

import config

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
server_socket.bind((config.MANIPULATOR_HOST, config.MANIPULATOR_PORT))

# Начинаем прослушивание
server_socket.listen()

print(f"Сервер манипулятора слушает на {config.MANIPULATOR_HOST}:{config.MANIPULATOR_PORT}...")

while True:
    # Принимаем новое соединение
    client_socket, client_address = server_socket.accept()
    print(f"Принято соединение от {client_address}")

    # Получаем данные от клиента
    data = client_socket.recv(1024)
    print(f"Получены данные: {data.decode()}")

    # Закрываем соединение с клиентом
    client_socket.close()

# Закрываем серверный сокет
server_socket.close()
