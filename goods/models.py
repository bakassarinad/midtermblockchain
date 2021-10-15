from django.db import models

class Good(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.name}'