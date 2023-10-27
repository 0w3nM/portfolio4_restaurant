from .models import Reservation
import datetime
from django import forms
from django.forms import ModelForm

TIME_CHOICES = [
    ('time1', "17:00"),
    ('time2', "17:15"),
    ('time3', "17:30"),
    ('time4', "18:45"),
    ('time5', "18:00"),
    ('time6', "18:15"),
    ('time7', "18:30"),
    ('time8', "18:45"),
    ('time9', "19:00"),
    ('time10', "19:15"),
    ('time11', "19:30"),
    ('time12', "19:45"),
    ('time13', "20:00"),
    ('time14', "20:15"),
    ('time15', "20:30"),
    ('time16', "20:45"),
]


PARTY_SIZE = [
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7),
    (8),
    (9),
    (10),
]


class ReservationForm(ModelForm):
    """
    Reservation Form
    """
    name = forms.CharField(label='Enter Name ', required=True, max_length=25)

    day = forms.DateField(initial=datetime.date.today)

    time = forms.ChoiceField(label='Time ', choices=TIME_CHOICES)

    party_size = forms.ChoiceField(label='Party Members ', choices=PARTY_SIZE)

    class Meta:
        model = Reservation
        fields = '__all__'
