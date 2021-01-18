from django.urls import path
from .views import RoomList, BookingList, HotelList
from . import views

app_name = 'hotel'

urlpatterns = [
    path('',views.home, name='home'),
    path('room_list/',RoomList.as_view(),name='RoomList'),
    path('booking_list/',BookingList.as_view(),name='BookingList'),
    path('hotel_list/',HotelList.as_view(),name='HotelList'),
]
