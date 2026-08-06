from pydantic import BaseModel, Field
from typing import Literal


class NotificationRequest(BaseModel):
    """
    Modelo de validación para la petición de envío de notificación (Request Body).
    Garantiza que todos los parámetros sean obligatorios y cumplan con los formatos esperados.
    """
    userId: str = Field(..., min_length=1, description="ID único del usuario destinatario")
    message: str = Field(..., min_length=1, description="Contenido o mensaje de la notificación")
    channel: Literal["email", "sms"] = Field(..., description="Canal de envío permitido ('email' o 'sms')")


class NotificationResponse(BaseModel):
    """
    Modelo para estructurar la respuesta de una notificación o el registro dentro del historial.
    """
    userId: str
    message: str
    channel: str