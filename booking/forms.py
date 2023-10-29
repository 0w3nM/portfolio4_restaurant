from .models import Reservation
from django.forms.widgets import NumberInput
from django import forms
from .models import PARTY_SIZE, TIMES_AVAILABLE
from django.forms import ModelForm


class ReservationForm(ModelForm):
    """
    Reservation Form
    """
    name = forms.CharField(label='Enter Name ', required=True, max_length=25)

    day = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    time = forms.ChoiceField(choices=TIMES_AVAILABLE)

    party_size = forms.ChoiceField(choices=PARTY_SIZE)

    class Meta:
        model = Reservation
        fields = '__all__'
