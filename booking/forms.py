from django import forms
import datetime
from .models import Reservation

TIME_CHOICES = [
    ("17:00", "17:15"),
    ("17:30", "17:45"),
    ("18:00", "18:15"),
    ("18:30", "18:45"),
    ("19:00", "19:15"),
    ("19:30", "19:45"),
    ("20:00", "20:15"),
    ("20:30", "20:45"),
]


PARTY_SIZE = [
    ('1', '2'),
    ('3', '4'),
    ('5', '6'),
    ('7', '8'),
    ('9', '10'),
]


class ReservationForm(forms.ModelForm):
    """
    Reservation Form
    """
    name = forms.CharField(label='Enter Name: ', required=True, max_length=25)

    day = forms.DateField(initial=datetime.date.today)

    time = forms.ChoiceField(label='Time: ', choices=TIME_CHOICES)

    party_size = forms.ChoiceField(label='Party Members: ', choices=PARTY_SIZE)
