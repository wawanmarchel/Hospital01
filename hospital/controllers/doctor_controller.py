from django.shortcuts import render
from hospital.models.doctor import Doctor
from hospital.models.nurse import Nurse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == "POST":
        req = request.POST.dict()
        name = req['name']
        doctors = Doctor.objects.filter(first_name__contains=name).order_by('first_name')
        nurses = Nurse.objects.all().order_by('first_name')
    else:
        doctors = Doctor.objects.all().order_by('first_name')
        nurses = Nurse.objects.all().order_by('first_name')
    data = {
        'doctors': doctors,
        'nurses': nurses,
    }
    return render(request, 'doctor/index.html', data)
