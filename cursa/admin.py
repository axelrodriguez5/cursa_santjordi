"""
Configuració del panell d'administració de Django.
Aquí registrem els models perquè es puguin gestionar des de /admin/.
"""
from django.contrib import admin
from .models import Categoria, Participant


# El decorador @admin.register registra el model i aplica la configuració alhora
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Columnes que es mostren a la llista del panell admin
    list_display = ('nom', 'edat_minima', 'edat_maxima', 'distancia_km')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('dorsal', 'nom', 'cognoms', 'categoria', 'temps_segons')
    list_filter = ('categoria',)              # Filtre lateral per categoria
    search_fields = ('nom', 'cognoms', 'dorsal')  # Caixa de cerca per aquests camps