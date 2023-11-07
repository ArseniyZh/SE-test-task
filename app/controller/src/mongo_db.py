from pymongo import MongoClient

from . import config

# Создаем подключение к MongoDB
client = MongoClient(f"{config.DB_HOST}://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_NAME}:27017/")
db = client.db
signals = db.my_signals
control_signals = db.my_control_signals
