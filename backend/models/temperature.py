from pydantic import BaseModel
from datetime import datetime

class Temperature(BaseModel):
    value: float
    timestamp: datetime