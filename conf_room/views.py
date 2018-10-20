from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from .forms import *
from django.contrib import messages
from .models import Room
from datetime import datetime


class AddRoom(View):
    form_class = AddRoomForm
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'conf_room/room_add.html',
                      {'form': self.form_class, 'rooms': rooms, 'title': 'Dodaj sale'})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dodano salę')
            return redirect('room-all')
        messages.error(request, 'Błędne dane')
        return HttpResponse('Nieprawidłowe dane')


class ModifyRoom(View):
    form_class = AddRoomForm

    def get(self, request, id_room):
        room = get_object_or_404(Room, id=id_room)
        rooms = Room.objects.all()
        initial = {
            'name': room.name,
            'capacity': room.capacity,
            'projector': room.projector,
            'tv': room.tv,
            'air_conditioning': room.air_conditioning,
        }
        form = self.form_class(initial=initial)
        return render(request, 'conf_room/room_add.html', {'form': form, 'rooms': rooms, 'title': 'Edytuj sale'})

    def post(self, request, id_room):
        room = get_object_or_404(Room, id=id_room)
        form = self.form_class(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Zmieniono dane')
        return redirect('room-all')


class RoomShow(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'conf_room/home.html', {'rooms': rooms})


class RoomDetails(View):

    def get(self, request, id_room):
        room = get_object_or_404(Room, id=id_room)
        rooms = Room.objects.all()
        return render(request, 'conf_room/room_details.html', {'room_det': room, 'rooms': rooms})


class RoomReserv(View):
    form_class = AddReservForm

    def get(self, request, id_room):
        room = get_object_or_404(Room, id=id_room)
        rooms = Room.objects.all()
        return render(request, 'conf_room/room_reservation.html', {'room_det': room, 'rooms': rooms, 'form': self.form_class})

    def post(self, request, id_room):
        form = self.form_class(request.POST)
        room = get_object_or_404(Room, id=id_room)
        if form.is_valid():
            reservation_db = list(Reservation.objects.filter(rooms_id=room, date=form.instance.date))
            if not reservation_db and form.instance.date >= datetime.date(datetime.now()):
                messages.success(request, 'Rezerwacja dokonana')
                Reservation.objects.create(date=form.instance.date, rooms=room, comment=form.instance.comment)
            else:
                messages.warning(request, 'Podano złą datę')
                return redirect('room-details', id_room)
        else:
            messages.warning(request, 'Błędne dane')
            return redirect('room-details', id_room)
        return redirect('room-all')



def delete_room(request, id_room):
    room = get_object_or_404(Room, id=id_room)
    name = room.name
    if room:
        room.delete()
        messages.success(request, f'Usunięto salę {name}')
        return redirect('room-all')
