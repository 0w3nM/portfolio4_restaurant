from django.shortcuts import render
from django.views import generic
from .models import Booking


def index(request):
    return render(request, "index.html")


class BookingList(generic.ListView):
    model = Booking
    template_name = 'booking.html'
