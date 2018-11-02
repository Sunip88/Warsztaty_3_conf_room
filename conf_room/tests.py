from django.test import TestCase, Client
from conf_room.models import Room
from .forms import *
from django.urls import reverse
from conf_room.views import AddRoom

# Create your tests here.


class RoomTest(TestCase):

    def create_room(self, name='testing room', capacity=250, projector=True, tv=True, air_conditioning=True):
        return Room.objects.create(name=name, capacity=capacity, projector=projector, tv=tv,
                                   air_conditioning=air_conditioning)

    def test_room_creation(self):
        r = self.create_room()
        self.assertTrue(isinstance(r, Room))
        self.assertEqual(r.__str__(), r.name)

    def test_add_room_view(self):
        resp = self.client.get('http://127.0.0.1:8000/room/new/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'conf_room/room_add.html')

    def test_add_room_view_form_valid(self):
        form = AddRoomForm(data={'name': 'testowy', 'capacity': 250, 'projector': True, 'tv': False, 'air_conditioning': True})
        self.assertTrue(form.is_valid())


