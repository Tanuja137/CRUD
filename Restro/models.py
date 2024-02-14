

# Create your models here.
# models.py
# models.py
from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"Order for {self.name} - {self.food_item}"
