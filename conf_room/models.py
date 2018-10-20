from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)


class Reservation(models.Model):
    date = models.DateField()
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField()
