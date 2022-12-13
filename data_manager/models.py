from django.db import models
from data_entry.models import BaseModel

class Countries(BaseModel):
    name = models.CharField(max_length=255, unique=True)

class Events(BaseModel):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, verbose_name="event_country")
    title = models.CharField(max_length=255)
    date = models.DateField()
    notes = models.TextField(null=True, blank=True)
    bunting = models.BooleanField(default=False)
