from django.shortcuts import render
from .models import Componentes
# Create your views here.





def home(request):
    componentes = Componentes.objects.all()
    context = {'componentes': componentes}
    return render(request, 'base/home.html', context)

def tabela(request, pk):
    componente = Componentes.objects.get(id=pk)
    context = {'componente':componente}
    return render(request, 'base/tabela.html', context)

