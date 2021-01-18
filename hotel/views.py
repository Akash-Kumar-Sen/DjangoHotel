from django.shortcuts import render
from django.views.generic import ListView
from .models import Room,Booking,Hotel

# Create your views here.
def home(request):
    return render(request, 'hotel/home.html', {})

class HotelList(ListView):
    model = Hotel

class RoomList(ListView):
    model = Room

class BookingList(ListView):
    model = Booking