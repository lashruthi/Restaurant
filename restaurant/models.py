
from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
