from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    description = models.TextField()
    promotion = models.DecimalField(max_digits=10, decimal_places=5)
    quantity = models.IntegerField()
    seasonality = models.CharField(max_length=100, null=True, blank=True)
    profile = models.CharField(max_length=50, null=True, blank=True)
    diameter = models.CharField(max_length=100)
    speed_index = models.CharField(max_length=100)
    load_indices = models.IntegerField()
    load_indices_for_double = models.IntegerField()
    characteristics = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.id}"
