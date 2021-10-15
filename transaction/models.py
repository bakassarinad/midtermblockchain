from django.db import models


from django.db.models.deletion import CASCADE
from goods.models import Good
from users.models import User

class Order(models.Model):
    
    time_start = models.DateField(auto_now_add=True)
    packaging = models.IntegerField(default=3)
    transit = models.IntegerField(default=5)
    good = models.ForeignKey(Good, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE, default=1)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30, default='not confirmed')

