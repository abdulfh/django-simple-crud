from django.db import models
from cars.models import Car
from authentication.models import User

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    pickUpLoc = models.CharField(max_length=100)
    dropOffLoc = models.CharField(max_length=100)
    pickUpDate = models.DateField()
    dropOffDate = models.DateField()
    pickUpTime = models.TimeField()
    carId = models.ForeignKey(Car, on_delete=models.RESTRICT, unique=False)
    userId = models.ForeignKey(User, on_delete=models.RESTRICT,null=True, unique=False)
    adminId = models.IntegerField(null=True)
