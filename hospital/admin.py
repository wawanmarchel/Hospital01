from django.contrib import admin
from hospital.models import doctor, patient, medicine, nurse, room, medecine_type

admin.site.register(doctor.Doctor)
admin.site.register(patient.Patient)
admin.site.register(medicine.Medicine)
admin.site.register(room.Room)
admin.site.register(nurse.Nurse)
admin.site.register(medecine_type.Medicine_type)
# Register your models here.
