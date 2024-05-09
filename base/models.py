from django.db import models

# Create your models here.

class Componentes(models.Model):
    nome = models.CharField(max_length=100)
    unidade_de_medida = models.CharField(max_length=10)
    #updated = models.DateTimeField(auto_now=True) salva quando foi updateado
    #created = models.DateTimeField(auto_now_add=True) salva quando foi criado
    
    def ___str___(self):
        return self.name
