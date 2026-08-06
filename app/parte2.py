import sys
from pathlib import Path

# --- Configuración del Entorno y Rutas ---
# Obtiene la ruta absoluta de la carpeta raíz del proyecto (PRUEBA)
root_path = Path(__file__).resolve().parent.parent

# Agrega la carpeta raíz al sys.path para que Python pueda resolver las importaciones del paquete 'app'
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from fastapi import FastAPI, HTTPException, status
from app.models import NotificationRequest, NotificationResponse
from app.services import NotificationFactory
from app.database import save_notification, get_all_notifications

# Inicialización de la aplicación FastAPI con título y versión para la documentación interactiva
app = FastAPI(title="Notification System API", version="1.0.0")


# --- Endpoint POST: Envío de Notificaciones ---
@app.post("/notifications", status_code=status.HTTP_201_CREATED)
def send_notification(payload: NotificationRequest):
    """
    Recibe los datos de una notificación, selecciona la estrategia correspondiente
    según el canal (Email/SMS) y guarda el envío en el historial.
    """
    try:
        # Obtiene la estrategia adecuada (Email o SMS) usando el patrón Factory
        strategy = NotificationFactory.get_strategy(payload.channel)
        
        # Ejecuta la lógica de envío mediante el patrón Strategy
        strategy.send(payload.userId, payload.message)
        
        # Convierte el modelo Pydantic a diccionario para persistir en la base de datos
        record = payload.model_dump()
        save_notification(record)
        
        return {"status": "success", "message": "Notificación enviada correctamente"}
    except ValueError as e:
        # Captura errores de negocio (ej. canal no soportado) y los retorna como HTTP 400 Bad Request
        raise HTTPException(status_code=400, detail=str(e))


# --- Endpoint GET: Consulta del Historial ---
@app.get("/notifications")
def list_notifications():
    """
    Recupera el historial completo de notificaciones enviadas.
    """
    data = get_all_notifications()
    return {"data": data}


# --- Bloque de Ejecución Directa ---
if __name__ == "__main__":
    import uvicorn

    # Inicia el servidor ASGI Uvicorn en localhost:8000
    uvicorn.run("app.parte2:app", host="127.0.0.1", port=8000)