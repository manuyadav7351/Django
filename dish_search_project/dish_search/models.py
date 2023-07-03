from django.db import models

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    lat_long = models.CharField(max_length=255)
    full_details = models.TextField()
    items = models.ManyToManyField('Items')

class Items(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5)