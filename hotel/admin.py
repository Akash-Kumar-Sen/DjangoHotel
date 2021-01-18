from django.contrib import admin

# Register your models here.
from .models import RoomType, Hotel, Room, Booking

admin.site.register(RoomType)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)