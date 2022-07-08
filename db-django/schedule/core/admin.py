from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao') #shows the fields we want to see
    list_filter = ('usuario','data_evento') # add a filter to search

admin.site.register(Evento, EventoAdmin)
