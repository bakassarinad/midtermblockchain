from django.db import models

class Good(models.Model):
    name = models.CharField(max_length=50, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    capacity = models.PositiveIntegerField(default=0)
    