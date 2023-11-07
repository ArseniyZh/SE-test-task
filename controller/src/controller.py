from datetime import datetime as dt

from fastapi import FastAPI
from typing import List, Dict, Union

from . import models, mongo_db
from .utils import merge_intervals

app = FastAPI()


@app.post("/api/receive_data")
async def receive_data(data: models.SensorData) -> Dict[str, Union[str, dt]]:
    """
    Эндпоинт для приема данных с сенсоров.
    """
    control_signal = {
        "datetime": data.datetime,
        "status": "up" if data.payload > 50 else "down"
    }
    control_signal["_id"] = str(mongo_db.signals.insert_one(control_signal).inserted_id)

    return control_signal


@app.get("/api/control_signals")
async def get_control_signals(start_time: str, end_time: str) -> List[str]:
    """
    Эндпоинт для вывода интервалов с сенсоров.
    """
    start_time = dt.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
    end_time = dt.strptime(end_time, "%Y-%m-%dT%H:%M:%S")

    result = mongo_db.control_signals.find({
        "start_time": {"$gte": start_time},
        "end_time": {"$lte": end_time},
    })

    control_signals = [
        {
            "_id": str(signal["_id"]),  # Преобразование ObjectId в строку
            "start_time": signal["start_time"],
            "end_time": signal["end_time"],
            "status": signal["status"],
        }
        for signal in result
    ]

    merged_signals = await merge_intervals(control_signals)

    return merged_signals


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
