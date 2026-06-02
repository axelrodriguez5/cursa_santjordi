from django.contrib import admin
from .models import Categoria, Participant


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'edat_minima', 'edat_maxima', 'distancia_km')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('dorsal', 'nom', 'cognoms', 'categoria', 'temps_segons')
    list_filter = ('categoria',)
    search_fields = ('nom', 'cognoms', 'dorsal')
