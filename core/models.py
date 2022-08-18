from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=1000, required=False)
    brand = models.CharField(max_length=1000, required=False)
    date = models.CharField(max_length=2000, required=False)
    image = models.JSONField(max_length=2000, required=False)
    tag = models.CharField(max_length=2000, required=False)
    rank = models.CharField(max_length=2000, required=False)
    description = models.JSONField(max_length=20000, required=False)
