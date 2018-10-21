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
    class_form = SearchForm
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'conf_room/home.html', {'rooms': rooms, 'form': self.class_form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            capacity = form.cleaned_data['capacity']
            projector = form.cleaned_data['projector']
            tv = form.cleaned_data['tv']
            air_cond = form.cleaned_data['air_conditioning']
            date = form.cleaned_data['date']

            if name:
                room_name = Room.objects.filter(name__icontains=name)
            else:
                room_name = Room.objects.all()

            if capacity:
                room_capacity = Room.objects.filter(capacity__gte=capacity)
            else:
                room_capacity = Room.objects.all()

            if projector:
                room_projector = Room.objects.filter(projector=projector)
            else:
                room_projector = Room.objects.all()

            if tv:
                room_tv = Room.objects.filter(tv=tv)
            else:
                room_tv = Room.objects.all()

            if air_cond:
                room_air_cond = Room.objects.filter(air_conditioning=air_cond)
            else:
                room_air_cond = Room.objects.all()

            rooms = room_name & room_capacity & room_projector & room_tv & room_air_cond
            if date:
                temp = []
                for room in rooms:
                    roomif = Reservation.objects.filter(date=date, rooms_id=room)
                    if len(roomif) == 0:
                        temp.append(room)
            else:
                temp = rooms

            url = '/?'
            for t in temp:
                a = f'{t.id}={t.name}'
                url += a

            # return redirect('search')
            # return redirect(f'search{url}')
            return render(request, 'conf_room/search_room.html', {'rooms': temp})



def search_show(request):

    return render(request, 'conf_room/search_room.html')


class RoomDetails(View):

    def get(self, request, id_room):
        room = get_object_or_404(Room, id=id_room)
        rooms = Room.objects.all()
        time_now = datetime.date(datetime.now())
        reservations = Reservation.objects.filter(rooms_id=room, date__gt=time_now)
        return render(request, 'conf_room/room_details.html', {'room_det': room, 'rooms': rooms, 'reservations': reservations})


class RoomReserv(View):
    form_class = AddReservForm

    def get(self, request, id_room):
        room = get_object_or_404(Room, id=id_room)
        rooms = Room.objects.all()
        time_now = datetime.date(datetime.now())
        reservations = Reservation.objects.filter(rooms_id=room, date__gt=time_now)
        return render(request, 'conf_room/room_reservation.html',
                      {'room_det': room, 'rooms': rooms, 'form': self.form_class, 'reservations': reservations})

    def post(self, request, id_room):
        form = self.form_class(request.POST)
        room = get_object_or_404(Room, id=id_room)
        if form.is_valid():
            date_form = form.cleaned_data['date']
            reservation_db = list(Reservation.objects.filter(rooms_id=room, date=date_form))
            if not reservation_db and date_form >= datetime.date(datetime.now()):
                messages.success(request, 'Rezerwacja dokonana')
                Reservation.objects.create(date=date_form, rooms=room, comment=form.cleaned_data['comment'])
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
