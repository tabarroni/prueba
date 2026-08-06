import sys
from pathlib import Path

# Añade la carpeta raíz (PRUEBA) al path de Python
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

import pytest
from fastapi.testclient import TestClient
from app.parte2 import app

client = TestClient(app)

def test_tc01_create_email_notification_success():
    payload = {"userId": "123", "message": "Hola Email", "channel": "email"}
    response = client.post("/notifications", json=payload)
    assert response.status_code == 201
    assert response.json()["status"] == "success"

def test_tc02_create_sms_notification_success():
    payload = {"userId": "124", "message": "Hola SMS", "channel": "sms"}
    response = client.post("/notifications", json=payload)
    assert response.status_code == 201

def test_tc03_invalid_channel():
    payload = {"userId": "125", "message": "Hola Invalid", "channel": "push"}
    response = client.post("/notifications", json=payload)
    assert response.status_code == 422  # Error de validación de Pydantic

def test_tc04_missing_required_fields():
    payload = {"userId": "126", "channel": "email"}
    response = client.post("/notifications", json=payload)
    assert response.status_code == 422

def test_tc05_get_notifications_history():
    response = client.get("/notifications")
    assert response.status_code == 200
    assert "data" in response.json()
    assert isinstance(response.json()["data"], list)