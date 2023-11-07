import asyncio
import datetime
import random
import pytz

import aiohttp

from config import (
    SENSOR_COUNT,
    MESSAGES_PER_SECOND,
    CONTROLLER_URL,
)


async def generate_sensor_data(sensor_id: int) -> None:
    """
    Функция для генерации сенсора и сообщения.

    :param sensor_id: ID сенсора
    :return: None
    """
    while True:
        current_time = datetime.datetime.now(tz=pytz.timezone("Europe/Moscow"))
        current_time = current_time.strftime('%Y-%m-%dT%H:%M:%S')
        payload = random.randint(1, 100)
        data = {"datetime": current_time, "payload": payload}
        await send_message(sensor_id, data)
        await asyncio.sleep(1 / MESSAGES_PER_SECOND)


async def send_message(sensor_id: int, data: dict) -> dict:
    """
    Функция для отправки сообщения от определенного сенсора.

    :param sensor_id: ID сенсора
    :param data: JSON, который отправляем
    :return: Словарь с данными о результате запроса
    """
    _sensor_id = "sensor_id"
    message = "message"
    status = "status"
    return_data = {
        _sensor_id: sensor_id,
        message: None,
        status: None
    }

    url = f"{CONTROLLER_URL}/api/receive_data"

    response_status = None
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url=url, json=data) as response:
                response_status = response.status
                if response.status == 200:
                    response_message = f"Sensor {sensor_id} sent message: {data}"
                else:
                    response_message = f"Sensor {sensor_id} failed to send message. Status code: {response_status}"
        except Exception as e:
            response_message = f"Sensor {sensor_id} failed to send message: {str(e)}"

    print(response_message)

    return_data[message] = response_message
    return_data[status] = response_status

    return return_data


async def main():
    """
    Входная точка программы.

    :return:
    """
    tasks = []
    for sensor_id in range(1, SENSOR_COUNT + 1):
        task = asyncio.create_task(generate_sensor_data(sensor_id))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
