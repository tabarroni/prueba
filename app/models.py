from pydantic import BaseModel, Field
from typing import Literal

class NotificationRequest(BaseModel):
    userId: str = Field(..., min_length=1, description="ID del usuario")
    message: str = Field(..., min_length=1, description="Mensaje a enviar")
    channel: Literal["email", "sms"] = Field(..., description="Canal de envío")

class NotificationResponse(BaseModel):
    userId: str
    message: str
    channel: str