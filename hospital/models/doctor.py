from django.db import models
from hospital.models.nurse import Nurse

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('DIED', null=True, blank=True)
    gender = models.CharField(max_length=100)
    nurse = models.ForeignKey(Nurse,on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'hospital'
    
    def __str__(self):
        return f'{self.first_name},{self.last_name}'