from django.urls import path, include
from .views import *

urlpatterns = [
    path('room/new/', AddRoom.as_view(), name='room-add'),
    path('', RoomShow.as_view(), name='room-all'),
    path('room/modify/<int:id_room>/', ModifyRoom.as_view(), name='room-modify'),
    path('room/delete/<int:id_room>/', delete_room, name='room-delete'),
    path('room/<int:id_room>/', RoomDetails.as_view(), name='room-details'),
    path('reservation/<int:id_room>/', RoomReserv.as_view(), name='room-reserv'),
    path('search/', search_show, name='search')
]