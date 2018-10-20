from django import forms
from .models import Room, Reservation
from django.contrib.admin.widgets import AdminDateWidget


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'projector', 'tv', 'air_conditioning']


class AddReservForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'comment']



