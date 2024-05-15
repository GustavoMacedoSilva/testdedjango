from django.shortcuts import render
from .models import Componentes
from .models import Rooms
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