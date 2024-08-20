from django.db import models

# Create your models here.

from django.db import models

class Meal(models.Model):
    meal_id = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    instructions = models.TextField()
    thumbnail = models.URLField(max_length=255)
    bill_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.name


