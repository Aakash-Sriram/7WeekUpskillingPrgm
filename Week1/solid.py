## EXAMPLE BAD CODE
"""
class NotificationService:
    def send_notification(self, notification_type, message):          -> One class handled all notification types.
        if notification_type == "email":
            print(f"Email: {message}")

        elif notification_type == "sms":
            print(f"SMS: {message}")

        elif notification_type == "push":
            print(f"Push Notification: {message}")


service = NotificationService()
service.send_notification("email", "Welcome")
"""

from abc import ABC, abstractmethod

# Abstract interface for all message senders
class MessageSender(ABC):

    # Every sender must implement this method
    @abstractmethod
    def send(self, message):
        pass


# Sends notifications through Email
class EmailSender(MessageSender):
    def send(self, message):
        print(f"Email: {message}")


# Sends notifications through SMS
class SmsSender(MessageSender):
    def send(self, message):
        print(f"SMS: {message}")


# Sends notifications through Push Notifications
class PushSender(MessageSender):
    def send(self, message):
        print(f"Push Notification: {message}")


# Notification service depends on the abstraction (MessageSender)
class NotificationService:

    # Dependency is injected through the constructor
    def __init__(self, sender):
        self.sender = sender

    # Uses the sender without knowing its concrete type
    def notify(self, message):
        self.sender.send(message)


# Create service with EmailSender dependency
service = NotificationService(EmailSender())

# Send notification
service.notify("Welcome")
