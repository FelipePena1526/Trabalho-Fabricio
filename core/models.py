from django.db import models
from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    local = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, related_name='participantes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
