from django.shortcuts import render, redirect, get_object_or_404
from . import views
from django.views import generic, View
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm


# View the Home Page #
def home(request):
    return render(request, 'index.html')

# View Reservations #


class ReservationList(generic.ListView):
    model = Reservation
    template_name = 'bookings.html'
    queryset = Reservation.objects.all()
    paginate_by = 5


# Create Reservation #

def create_reservation(request):
    """
    User can create a reservation
    """
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(request, 'Your reservation was successul.')
            return redirect('bookings')
        else:
            messages.error(request,
                           'Reservation wasnt successful. Please amend and try again.')
    else:
        reservation_form = ReservationForm()
    context = {
        'form': reservation_form
    }
    return render(request, 'create_reservation.html', context)


# Update Reservation #

def update_reservation(request, booking_id):
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
        return render(request, 'update_reservation.html', context)


# Delete Reservation #

def remove_reservation(request, booking_id):
    """
    User can delte a reservation
    """
    booking = get_object_or_404(Reservation, id=booking_id)
    booking.delete()
    messages.success(request,
                     'Your reservation has been sucessfully deleted')
    return redirect('bookings')
