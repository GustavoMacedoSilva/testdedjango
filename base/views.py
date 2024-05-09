from django.shortcuts import render

# Create your views here.

rooms = [
    {'id' :1, 'name':'Opção1'},
    {'id' :2, 'name':'Opção2'},
    {'id' :3, 'name':'Opção3'},
]



def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', {'rooms': rooms})

def tabela(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/tabela.html', context)

