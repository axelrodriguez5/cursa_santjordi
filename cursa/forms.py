from django import forms
from .models import Participant, Categoria


class FormulariParticipant(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['nom', 'cognoms', 'dorsal', 'email',
                  'data_naixement', 'categoria', 'temps_segons']
        widgets = {
            'data_naixement': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'nom': 'Nom',
            'cognoms': 'Cognoms',
            'dorsal': 'Dorsal',
            'email': 'Correu electrònic',
            'data_naixement': 'Data de naixement',
            'categoria': 'Categoria',
            'temps_segons': 'Temps (segons)',
        }


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
