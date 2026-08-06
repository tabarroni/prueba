# Almacenamiento en memoria para el historial de notificaciones
history = []

def save_notification(data: dict):
    history.append(data)

def get_all_notifications() -> list:
    return history