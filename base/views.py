from django.shortcuts import render, redirect
from .models import Componentes
from .models import Rooms, Topic
from .forms import RoomForm
from django.db.models import Q
# Create your views here.





def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Rooms.objects.filter(
        Q(topic__nome__icontains=q) |
        Q(nome__icontains=q) |
        Q(descricao__icontains=q)
        )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics':topics, 'room_count':room_count}
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

def deleteRoom(request, pk):
    room = Rooms.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})