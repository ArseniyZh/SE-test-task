from datetime import datetime

from typing import List, Dict, Union


async def merge_intervals(signals: List[Dict[str, Union[str, datetime]]]) -> List[str]:
    """
    Функция для объединения сигналов в интервалы.

    :param signals: Список сигналов в формате [{"start_time": str, "end_time": str, "status": str}].
    :return: Список интервалов.
    """
    start_time = "start_time"
    end_time = "end_time"
    status = "status"

    # Обрабатываем корнер кейсы
    if not signals:
        return []
    if len(signals) == 1:
        signal = signals[0]
        return [f"{signal[start_time]} - {signal[end_time]} {signal[status]}"]

    result_list = []

    # Объединяем сигналы в интервалы
    current_signal = signals[0]
    for signal in signals[1:]:
        if current_signal[status] != signal[status]:
            result_list.append(f"{current_signal[start_time]} - {signal[start_time]} {current_signal[status]}")
            current_signal = signal

    if not result_list:  # Если попались все одного статуса
        result_list.append(f"{signals[0][start_time]} - {signals[-1][end_time]} {current_signal[status]}")

    return result_list
