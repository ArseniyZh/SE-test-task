# Используем базовый образ Python
FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /src

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем исходный код сенсора в контейнер
COPY . .

# Определяем порт, на котором будет работать сенсор
EXPOSE 8080

# Запускаем сенсор
CMD ["python", "src/sensor.py"]
