from django.db import models

# Create your models here.

class Restaurent(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    items = models.JSONField()
    lat_long = models.CharField(max_length=100)
    full_details = models.JSONField()

    def __str__(self):
        return self.name