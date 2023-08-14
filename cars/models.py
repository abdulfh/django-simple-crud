from django.db import models

# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    carType = models.CharField(max_length=10)
    rating = models.FloatField()
    fuel = models.CharField(max_length=10)
    image = models.CharField(max_length=200)
    hourRate = models.IntegerField()
    dayRate = models.IntegerField()
    monthRate = models.IntegerField()