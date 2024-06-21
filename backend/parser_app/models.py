from django.db import models


class TelegramMessage(models.Model):
    channel = models.CharField(max_length=255)
    message_id = models.IntegerField(unique=True)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.channel} - {self.message_id}"