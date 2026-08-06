from abc import ABC, abstractmethod

# Interfaces y Estrategias (Pattern Strategy)
class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, user_id: str, message: str) -> None:
        pass

class EmailNotificationStrategy(NotificationStrategy):
    def send(self, user_id: str, message: str) -> None:
        # Lógica simulada de envío de Email
        print(f"[EMAIL] Enviando correo a usuario {user_id}: {message}")

class SmsNotificationStrategy(NotificationStrategy):
    def send(self, user_id: str, message: str) -> None:
        # Lógica simulada de envío de SMS
        print(f"[SMS] Enviando SMS a usuario {user_id}: {message}")

# Factory (Pattern Factory)
class NotificationFactory:
    _strategies = {
        "email": EmailNotificationStrategy(),
        "sms": SmsNotificationStrategy()
    }

    @classmethod
    def get_strategy(cls, channel: str) -> NotificationStrategy:
        strategy = cls._strategies.get(channel.lower())
        if not strategy:
            raise ValueError(f"Canal no soportado: {channel}")
        return strategy