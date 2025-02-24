from pydantic import BaseModel
from datetime import datetime

class TemperatureSchema(BaseModel):
    temperature: float
    timestamp: datetime
