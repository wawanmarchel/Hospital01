from django.shortcuts import render
from hospital.models.patient import Patient
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    patients = Patient.objects.all()
    data = {
        'patients': patients,
    }
    return render(request, 'patient/index.html', context=data)
