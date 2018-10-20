from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .forms import *
from django.contrib import messages


class AddRomm(View):
    form_class = AddRoomForm

    def get(self, request):
        return render(request, 'conf_room/room_add.html',
                      {'form': self.form_class})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dodano salę')
            return redirect('room-add')
        messages.error(request, 'Błędne dane')
        return HttpResponse('Nieprawidłowe dane')