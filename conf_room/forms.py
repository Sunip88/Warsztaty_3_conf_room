from django import forms
from .models import Room, Reservation


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'projector']


class AddReservForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'comment']

