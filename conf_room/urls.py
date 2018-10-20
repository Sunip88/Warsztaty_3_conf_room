from django.urls import path, include
from .views import *

urlpatterns = [
    path('room/new/', AddRomm.as_view(), name='room-add'),
]