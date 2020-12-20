from django.db import models
from hospital.models.doctor import Doctor
from hospital.models.room import Room

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('DIED', null=True, blank=True)
    gender = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    about_illness = models.CharField(max_length=300)
    room = models.ForeignKey(Room,null=True,on_delete=models.SET_NULL)

    class Meta:
        app_label = 'hospital'

    def __str__(self):
        return f'{self.first_name},{self.last_name}'