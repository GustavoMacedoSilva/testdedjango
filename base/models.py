from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Componentes(models.Model):
    nome = models.CharField(max_length=100)
    unidade_de_medida = models.CharField(max_length=10)
    #updated = models.DateTimeField(auto_now=True) salva quando foi updateado
    #created = models.DateTimeField(auto_now_add=True) salva quando foi criado
    
    def __str__(self):
        return self.nome


class Topic(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Rooms(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created'] #faz a ordem de updated mais recente aparecer primeiro

    def __str__(self):
        return self.nome
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]