from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm

# View Reservations #


class ReservationList(generic.View):
    model = Reservation
    template_name = 'bookings.html'

# Create Reservation #


def create_reservation(self, request):
    """
    User can crate a reseration
    """
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.instance.name = request.user
            reservation_form.save()
            messages.success(request, 'Your reservation was successul.')
            return redirect('bookings')
        else:
            messages.error(request,
            'Reservation wasnt successful. Please amend and try again.')
            reservation_form = ReservationForm()
            context = {
                'form': reservation_form
            }
        return render(request, '/templates/create_reservation')

# Update Reservation #


def update_reservation(self, request, booking_id):
    """
    User can amend a reservation
    """
    booking = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            messages.success(request, 
                'Your reservation was successully updated.')
            return redirect('bookings')
        else:
            messages.error(request,
                'Reservation wsnt updated successfully. Please amend and try again.')
            reservation_form = ReservationForm()
            context = {
                'form': reservation_form
            }
        return render(request, '/templates/update_reservation')

# Delete Reservation #

def remove_reservation(self, request, booking_id):
    """
    User can delte a reservation
    """
    booking = get_object_or_404(Reservation, id=booking_id)
    booking.delete()
    messages.success(request,
    'Your reservation has been sucessfully deleted')       
    return redirect('bookings')
