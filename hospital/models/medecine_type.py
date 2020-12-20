from django.db import models

class Medicine_type(models.Model):
    medicine_type = models.CharField(max_length=100)

    class Meta:
        app_label = 'hospital'

    def __str__(self):
        return f'{self.medicine_type}'