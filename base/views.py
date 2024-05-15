from django.shortcuts import render, redirect
from .models import Componentes
from .models import Rooms
from .forms import RoomForm
# Create your views here.





def home(request):
    rooms = Rooms.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def tabela(request, pk):
    componente = Componentes.objects.get(id=pk)
    context = {'componente':componente}
    return render(request, 'base/tabela.html', context)

def room(request, pk):
    room = Rooms.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Rooms.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request, 'base/room_form.html', context)