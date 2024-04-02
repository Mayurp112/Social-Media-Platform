# managers.py
from django.db import models

class NotificationManager(models.Manager):
    def create_notification(self, user, notification_type):
        return self.create(user=user, notification_type=notification_type)
