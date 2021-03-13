from core.models import TimestampedModel
from django.db import models


class Valute(TimestampedModel):
    external_id = models.CharField(db_index=True, max_length=6, unique=True)
    num_code = models.CharField(max_length=10)
    char_code = models.CharField(max_length=4)
    nominal = models.IntegerField()
    name = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=10, decimal_places=4)
    previous = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return self.name
