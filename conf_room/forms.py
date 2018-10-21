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


class SearchForm(forms.Form):
    name = forms.CharField(max_length=64, required=False)
    capacity = forms.IntegerField(required=False, label='Ilość miejsc')
    date = forms.DateField(required=False)
    projector = forms.BooleanField(required=False)
    tv = forms.BooleanField(required=False)
    air_conditioning = forms.BooleanField(required=False)

