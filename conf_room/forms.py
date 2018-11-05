from django import forms
from .models import Room, Reservation
from django.forms.widgets import SelectDateWidget
from datetime import datetime


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'projector', 'tv', 'air_conditioning']


class AddReservForm(forms.ModelForm):
    year = datetime.today().year
    year_range = tuple([i for i in range(year, year + 2)])
    date = forms.DateField(label='Data', widget=SelectDateWidget(years=year_range))

    class Meta:
        model = Reservation
        fields = ['date', 'comment']
        help_texts = {
            'comment': 'np:. Jakiś komentarz.'
        }
        labels = {
            'comment': 'Komentarz'
        }


class SearchForm(forms.Form):
    year = datetime.today().year
    year_range = tuple([i for i in range(year, year + 3)])

    name = forms.CharField(max_length=64, required=False, label='Nazwa sali')
    capacity = forms.IntegerField(required=False, label='Minimalna ilość miejsc')
    date = forms.DateField(required=False, label='Data', widget=SelectDateWidget(years=year_range))
    projector = forms.BooleanField(required=False, label='Projektor')
    tv = forms.BooleanField(required=False, label='TV')
    air_conditioning = forms.BooleanField(required=False, label='Klimatyzacja')

