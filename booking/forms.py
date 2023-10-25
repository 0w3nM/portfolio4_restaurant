from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    """
    Reservation Form
    """
    name = forms.CharField(label="Enter Name", required=True, max_length=25)
    day = forms.()
    time = forms.()
    party_size = forms.IntegerField(widget=forms.TextInput(attrs={'title': 'Number: ' }))