#!/usr/bin/python3.7
from django import template
from datetime import datetime
from conf_room.models import Reservation

register = template.Library()


@register.filter(name='change_bool')
def trueorfalse(var_bool):
    if var_bool:
        return 'Tak'
    else:
        return 'Nie'


@register.filter(name='reserv_today')
def reservation_today(room_id):
    time = datetime.now()
    reserve = Reservation.objects.filter(rooms_id=room_id, date=time)
    if len(reserve) > 0:
        return 'Zajete'
    else:
        return 'Wolne'