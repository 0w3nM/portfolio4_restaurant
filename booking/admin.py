from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'day', 'time', 'party_size')
    list_filter = ('time', 'day', 'party_size')
    search_fields = ['name', 'day', 'time']