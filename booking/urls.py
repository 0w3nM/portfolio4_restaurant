from . import views
from django.urls import path
from booking.views import create_reservation, update_reservation, remove_reservation

app_name = 'booking'

urlpatterns = [
    path('', views.home, name='home'),
    path('bookings/', views.ReservationList.as_view(), name='bookings'),
    path('create_reservations/', views.create_reservation,
         name='create_reservations'),
    path('update_reservation/<int:reservation_id>', views.update_reservation,
         name='update_reservation'),
    path('remove_reservation/<int:reservation_id>/', views.remove_reservation,
         name='remove_reservation'),
]
