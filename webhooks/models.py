from core.models import TimestampedModel
from django.db import models


class Webhook(TimestampedModel):
    callback_url = models.CharField(max_length=256)

    def __str__(self):
        return self.callback_url
