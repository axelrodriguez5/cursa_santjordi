"""
Rutes (URLs) de l'app cursa.
Cada path connecta una URL amb la seva funció view corresponent.
"""
from django.urls import path
from . import views

urlpatterns = [
    # Pàgina d'inici
    path('', views.index, name='index'),

    # Rutes de participants (CRUD complet)
    path('participants/', views.llista_participants, name='llista_participants'),
    path('participants/afegir/', views.afegir_participant, name='afegir_participant'),
    # <int:id> captura un número de la URL i el passa com a paràmetre a la view
    path('participants/<int:id>/editar/', views.editar_participant, name='editar_participant'),
    path('participants/<int:id>/eliminar/', views.eliminar_participant, name='eliminar_participant'),

    # Rutes de categories
    path('categories/', views.llista_categories, name='llista_categories'),
    path('categories/afegir/', views.afegir_categoria, name='afegir_categoria'),

    # Classificació de resultats
    path('resultats/', views.resultats, name='resultats'),
]