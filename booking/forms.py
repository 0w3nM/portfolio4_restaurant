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
    ('p_num1', '1'),
    ('p_num2', '2'),
    ('p_num3', '3'),
    ('p_num4', '4'),
    ('p_num5', '5'),
    ('p_num6', '6'),
    ('p_num7', '7'),
    ('p_num8', '8'),
    ('p_num9', '9'),
    ('p_num10', '10'),
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
