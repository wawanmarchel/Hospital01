from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)
    room_price = models.IntegerField()
    class Meta:
        app_label = 'hospital'

    def __str__(self):
        return f'{self.room_name}'