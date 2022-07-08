from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_evento = models.DateTimeField(verbose_name='data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name= 'data da criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete parameter tells django
    local = models.CharField(max_length=100, null=True)                    # what to do if user is deleted

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime("%d/%m/%Y - %H:%M:%S")

    def get_data_input_evento(self):
        return self.data_evento.strftime("%Y-%m-%dT%H:%M") #input default