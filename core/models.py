from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    brand = models.CharField(max_length=1000, blank=True, null=True)
    date = models.CharField(max_length=2000, blank=True, null=True)
    images = models.CharField(max_length=2000, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.CharField(max_length=2000, blank=True, null=True)
    rank = models.CharField(max_length=2000, blank=True, null=True)
    description = models.CharField(max_length=2000000, blank=True, null=True)
