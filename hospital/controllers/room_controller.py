from django.shortcuts import render
from hospital.models.room import Room

def index(request):
    if request.method == "POST":
        req = request.POST.dict()
        name = req['name']
        rooms = Room.objects.filter(room_name__contains=name).order_by('room_name')
    else:
        rooms = Room.objects.all().order_by('room_name')
    data = {
        'rooms': rooms,
    }
    return render(request, 'room/index.html', data)