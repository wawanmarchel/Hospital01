from django.db import models
from hospital.models.medecine_type import Medicine_type

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    medicine_type = models.ForeignKey(Medicine_type,null=True,on_delete=models.SET_NULL,blank=True)
    
    class Meta:
        app_label = 'hospital'

    def __str__(self):
        return f'{self.name}'