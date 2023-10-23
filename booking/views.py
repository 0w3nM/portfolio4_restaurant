from django.shortcuts import render, redirect,get_object_or_404
from django.views import generic
from .models import Reservation


def index(request):
    return render(request, "index.html")


class BookingList(generic.ListView):
    model = Reservation
    template_name = 'booking.html'


class CreateReservation():
    model = Reservation
    template = 'create_reservation.html'

    def update_booking(self, request, booking_id):
        booking = get_object_or_404(Reservation, id=booking_id)

    def remove_booking(self, request, booking_id):
        booking = get_object_or_404(Reservation, id=booking_id)
        booking.delte()
        return redirect('bookings')
