from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
from goods.models import Good
from users.models import User

class Order(models.Model):
    name = models.CharField(max_length=50)
    Description = models.CharField(max_length=400)
    time_start = models.DateField(default=datetime.now)
    packaging = models.IntegerField(default=3)
    transit = models.IntegerField(default=5)
    good = models.ForeignKey(Good, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)

