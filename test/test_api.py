import sys
from pathlib import Path

# --- Configuración del Entorno de Pruebas ---
# Obtiene la ruta absoluta de la carpeta raíz del proyecto (PRUEBA)
root_path = Path(__file__).resolve().parent.parent

# Agrega la carpeta raíz al sys.path para permitir importar 'app.parte2' correctamente
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

import pytest
from fastapi.testclient import TestClient
from app.parte2 import app

# Inicialización del cliente de pruebas de FastAPI (simula peticiones HTTP en memoria sin levantar un servidor real)
client = TestClient(app)


# --- Casos de Prueba Automatizados (Parte 3) ---

def test_tc01_create_email_notification_success():
    """
    TC01: Validar el envío exitoso de una notificación por el canal 'email'.
    Espera respuesta HTTP 201 Created y confirmación de éxito.
    """
    payload = {"userId": "123", "message": "Hola Email", "channel": "email"}
    response = client.post("/notifications", json=payload)
    
    assert response.status_code == 201
    assert response.json()["status"] == "success"


def test_tc02_create_sms_notification_success():
    """
    TC02: Validar el envío exitoso de una notificación por el canal 'sms'.
    Espera respuesta HTTP 201 Created.
    """
    payload = {"userId": "124", "message": "Hola SMS", "channel": "sms"}
    response = client.post("/notifications", json=payload)
    
    assert response.status_code == 201


def test_tc03_invalid_channel():
    """
    TC03: Validar el rechazo de la petición cuando se ingresa un canal no permitido ('push').
    Espera respuesta HTTP 422 Unprocessable Entity generada por Pydantic/FastAPI.
    """
    payload = {"userId": "125", "message": "Hola Invalid", "channel": "push"}
    response = client.post("/notifications", json=payload)
    
    assert response.status_code == 422  # Error de validación de modelo/esquema


def test_tc04_missing_required_fields():
    """
    TC04: Validar el rechazo de la petición cuando falta un campo obligatorio ('message').
    Espera respuesta HTTP 422 Unprocessable Entity.
    """
    payload = {"userId": "126", "channel": "email"}
    response = client.post("/notifications", json=payload)
    
    assert response.status_code == 422


def test_tc05_get_notifications_history():
    """
    TC05: Validar la recuperación correcta del historial de notificaciones.
    Espera respuesta HTTP 200 OK y una estructura JSON con la clave 'data' de tipo lista.
    """
    response = client.get("/notifications")
    
    assert response.status_code == 200
    assert "data" in response.json()
    assert isinstance(response.json()["data"], list)