from django.db import models
from django.conf import settings
# Create your models here.

#Creating the hotel
class Hotel(models.Model):
    name = models.CharField(max_length=250)
    hotel_image = models.ImageField(upload_to='gallery')
    hotel_address = models.CharField(max_length=10000)
    hotel_policies = models.CharField(max_length=50000)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#Room and RoomType
class RoomType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_category = models.ForeignKey(RoomType,on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='gallery')
    hotel_name = models.ForeignKey(Hotel,on_delete=models.CASCADE,default=1)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.room_number


#Booking Model
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"{self.user} has booked {self.room} from {self.check_in} to {self.check_out}"
