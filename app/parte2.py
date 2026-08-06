from fastapi import FastAPI, HTTPException, status
from app.models import NotificationRequest, NotificationResponse
from app.services import NotificationFactory
from app.database import save_notification, get_all_notifications

app = FastAPI(title="Notification System API", version="1.0.0")

@app.post("/notifications", status_code=status.HTTP_201_CREATED)
def send_notification(payload: NotificationRequest):
    try:
        strategy = NotificationFactory.get_strategy(payload.channel)
        strategy.send(payload.userId, payload.message)
        
        record = payload.model_dump()
        save_notification(record)
        return {"status": "success", "message": "Notificación enviada correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/notifications")
def list_notifications():
    data = get_all_notifications()
    return {"data": data}