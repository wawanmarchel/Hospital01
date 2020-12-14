from django.shortcuts import render
from hospital.models.medicine import Medicine
from hospital.models.medecine_type import Medicine_type
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    medicines = Medicine.objects.all().order_by('medicine_type')
    medicine_types = Medicine_type.objects.all()
    data = {
        'medicines': medicines,
        'medicine_types': medicine_types,
    }
    return render(request, 'medicine/index.html', context=data)
