"""
Formularis de l'aplicació, creats amb ModelForm.
ModelForm genera els camps automàticament a partir d'un model.
"""
from django import forms
from .models import Participant, Categoria


# Formulari per afegir/editar participants
class FormulariParticipant(forms.ModelForm):
    class Meta:
        model = Participant  # Model en què es basa el formulari
        # Camps que es mostraran al formulari
        fields = ['nom', 'cognoms', 'dorsal', 'email',
                  'data_naixement', 'categoria', 'temps_segons']
        # Personalitzem el camp de data perquè mostri un selector de calendari
        widgets = {
            'data_naixement': forms.DateInput(attrs={'type': 'date'}),
        }
        # Etiquetes en català per als camps
        labels = {
            'nom': 'Nom',
            'cognoms': 'Cognoms',
            'dorsal': 'Dorsal',
            'email': 'Correu electrònic',
            'data_naixement': 'Data de naixement',
            'categoria': 'Categoria',
            'temps_segons': 'Temps (segons)',
        }


# Formulari per afegir/editar categories
class FormulariCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nom', 'edat_minima', 'edat_maxima', 'distancia_km']
        labels = {
            'nom': 'Nom de la categoria',
            'edat_minima': 'Edat mínima',
            'edat_maxima': 'Edat màxima',
            'distancia_km': 'Distància (km)',
        }