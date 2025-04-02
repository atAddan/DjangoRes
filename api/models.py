from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ApiUser(AbstractUser):
    ...
    
class Hotel(models.Model):
    name = models.CharField(max_length=128)
    
class Room(models.Model):
    num = models.PositiveBigIntegerField()
    hotel = models.ForeignKey(Hotel,related_name="rooms", on_delete=models.CASCADE)
    
class Booking(models.Model):
    room = models.ForeignKey(Room,related_name="Bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser,related_name="Bookings", on_delete=models.CASCADE)