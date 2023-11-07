# Используем базовый образ Python
FROM python:3.9

# Устанавливаем зависимости
RUN pip install fastapi[all] celery[redis]

# Создаем рабочую директорию внутри контейнера
WORKDIR /src

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем исходный код контроллера в контейнер
COPY . .

CMD ["sh", "-c", "uvicorn src.controller:app --host 0.0.0.0 --port 8080"]

# Expose the FastAPI port
EXPOSE 8080
