from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Componentes
from .models import Rooms, Topic, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RoomForm
from django.db.models import Q
# Create your views here.


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuario nao existe')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario ou senha não existe')
    
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    page = 'register'
    return render(request, 'base/login_register.html')


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

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Rooms.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('Vaza daqui amigo')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Rooms.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('Vaza daqui amigo')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})