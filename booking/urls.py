from . import views
from django.urls import path

app_name = 'booking'

urlpatterns = [
    path('', views.home, name='home'),
    path('bookings./', views.ReservationList.as_view(), name='bookings'),
    path('create_reservations/', views.create_reservation,
         name='create_reservations'),
    path('update_reservation/', views.update_reservation,
         name='update_reservation'),
    path('remove_reservation/', views.remove_reservation,
         name='remove_reservation'),
]
