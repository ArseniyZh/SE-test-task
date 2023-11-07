from datetime import datetime

from pydantic import BaseModel


class SensorData(BaseModel):
    payload: int
    datetime: datetime
