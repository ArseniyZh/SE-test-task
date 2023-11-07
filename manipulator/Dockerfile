# Используем базовый образ Python
FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /src

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем исходный код манипулятора в контейнер
COPY . .

# Определяем порт, на котором будет работать манипулятор
EXPOSE 8888

# Команда для запуска манипулятора
CMD ["python", "src/manipulator.py"]
