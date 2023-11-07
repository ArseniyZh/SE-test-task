import asyncio
import datetime
import json
import socket
import pytz

from typing import Dict, Union

from src import config, models
from src.celery_config import app
from .mongo_db import signals, control_signals

manipulator_host = config.MANIPULATOR_HOST
manipulator_port = config.MANIPULATOR_PORT

STOP = "stop"

@app.task
def send_to_manipulator() -> None:
    asyncio.run(send_data())


async def send_data():
    """
    Задача по управлению манипулятором.

    :return: None
    """
    control_signal = await get_data_for_manipulator()
    if control_signal == STOP:
        return

    control_signals.insert_one(control_signal)
    control_signal = json.dumps(control_signal["string"]).encode()
    try:
        # Создаем сокет
        controller_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        controller_socket.connect((manipulator_host, manipulator_port))

        controller_socket.send(control_signal)  # Отправляем данные

        controller_socket.close()  # Закрываем сокет
    except Exception as ex:
        print(ex)


async def get_data_for_manipulator() -> Dict[str, Union[str, datetime.datetime]]:
    """
    Получение контрольного сигнала для манипулятора.

    :return: Строка с данными контрольного сигнала.
    """
    _datetime = "datetime"
    status = "status"

    current_time = datetime.datetime.now(tz=pytz.timezone("Europe/Moscow"))
    interval_ago = (current_time - datetime.timedelta(seconds=config.MANIPULATOR_INTERVAL)).replace(tzinfo=None)

    # Поиск всех сигналов, записанных за последние n секунд и копирование их в список
    recent_signals = list(signals.find({_datetime: {"$gte": interval_ago}}))
    print("recent_signal", recent_signals[0])

    if not recent_signals:
        return STOP

    # Подсчет статусов и определение наиболее часто встречающегося статуса
    status_count = {}
    for signal in recent_signals:
        current_status = signal[status]
        status_count[current_status] = status_count.get(current_status, 0) + 1

    most_common_status = max(status_count, key=status_count.get)

    first_signal_time = recent_signals[0][_datetime]
    last_signal_time = recent_signals[-1][_datetime]

    # Создаем управляющий сигнал
    control_signal_string = f"{first_signal_time} - {last_signal_time} {most_common_status}"

    control_signal = {
        "string": control_signal_string,
        "start_time": first_signal_time,
        "end_time": last_signal_time,
        status: most_common_status,
    }

    return control_signal
