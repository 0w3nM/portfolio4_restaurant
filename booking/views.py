from django.shortcuts import render, redirect, get_object_or_404
from . import views
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm


# View the Home Page #
def home(request):
    return render(request, 'index.html')

# View Reservations #
class ReservationList(LoginRequiredMixin, generic.ListView):
    model = Reservation
    template_name = 'bookings.html'
    queryset = Reservation.objects.all()
    paginate_by = 5

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

# Create Reservation #
@login_required
def create_reservation(request):
    """
    User can create a reservation
    """
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():            
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.approved = False
            reservation.save()
            messages.success(request, 'Your reservation was successful.')
            return redirect('booking:bookings')
        else:
            messages.error(request, 'There is an error with your reservation. Please check all fields, amend and try again.')
    else:
        reservation_form = ReservationForm()
    context = {
        'form': reservation_form
    }
    return render(request, 'create_reservation.html', context)

# Update Reservation #
@login_required  
def update_reservation(request, reservation_id):
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


# Delete Reservation #
@login_required
def remove_reservation(request, reservation_id):
    """
    User can delete a reservation
    """
    booking = get_object_or_404(Reservation, id=reservation_id)
    booking.delete()
    messages.success(request,
                     'Your reservation has been sucessfully deleted')
    return redirect('booking:bookings')   
    
