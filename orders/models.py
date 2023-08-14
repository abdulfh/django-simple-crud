from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    pickUpLoc = models.CharField(max_length=100)
    dropOffLoc = models.CharField(max_length=100)
    pickUpDate = models.DateField()
    dropOffDate = models.DateField()
    pickUpTime = models.TimeField()
    carId = models.IntegerField()
    userId = models.IntegerField(null=True)
    adminId = models.IntegerField(null=True)
