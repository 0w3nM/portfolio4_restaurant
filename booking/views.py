from django.shortcuts import render, redirect, get_object_or_404
from . import views
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm


# View the Home Page #
def home(request):
    return render(request, 'index.html')

# View Reservations #

class ReservationList(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Reservation
    template_name = 'bookings.html'
    queryset = Reservation.objects.all()
    paginate_by = 5


    def test_func(self):
        """ Checks for user """"
        if self.request.user.is_user:
            return True
        else:
            return False


# Create Reservation #

def create_reservation(LoginRequiredMixin, UserPassesTestMixin, request):
    """
    User can create a reservation
    """
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(request, 'Your reservation was successful.')
            return redirect('booking:bookings')
        else:
            messages.error(request, 'Reservation wasnt successful. Please amend and try again.')
    else:
        reservation_form = ReservationForm()
    context = {
        'form': reservation_form
    }
    return render(request, 'create_reservation.html', context)

    def test_func(self):
        """ Checks for user """"
        if self.request.user.is_user:
            return True
        else:
            return False


# Update Reservation #

def update_reservation(LoginRequiredMixin, UserPassesTestMixin, request, reservation_id):
    """
    User can amend a reservation
    """
    booking = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            messages.success(request,
                             'Your reservation was successfully updated.')
            return redirect('booking:bookings')
        else:
            messages.error(request,
                           'Reservation wasnt updated successfully. Please amend and try again.')
            reservation_form = ReservationForm()
            context = {
                'form': reservation_form
            }
    else:
        reservation_form = ReservationForm()
    context = {
        'form': reservation_form
    }
    return render(request, 'update_reservation.html', context)

    def test_func(self):
        """ Checks for user """"
        if self.request.user.is_user:
            return True
        else:
            return False


# Delete Reservation #

def remove_reservation(LoginRequiredMixin, UserPassesTestMixin, request, reservation_id):
    """
    User can delete a reservation
    """
    booking = get_object_or_404(Reservation, id=reservation_id)
    booking.delete()
    messages.success(request,
                     'Your reservation has been sucessfully deleted')
    return redirect('booking:bookings')

    def test_func(self):
        """ Checks for user """"
        if self.request.user.is_user:
            return True
        else:
            return False
