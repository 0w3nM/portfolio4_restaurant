from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('create_reservations/', views.create_reservation, name='create_reservation'),
    path('update_reservation/', views.update_reservation, name='updat'),
    path('remove_reservation/', views.remove_reservation, name='remove_reservation'),
]