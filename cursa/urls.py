from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Participants
    path('participants/', views.llista_participants, name='llista_participants'),
    path('participants/afegir/', views.afegir_participant, name='afegir_participant'),
    path('participants/<int:id>/editar/', views.editar_participant, name='editar_participant'),
    path('participants/<int:id>/eliminar/', views.eliminar_participant, name='eliminar_participant'),

    # Categories
    path('categories/', views.llista_categories, name='llista_categories'),
    path('categories/afegir/', views.afegir_categoria, name='afegir_categoria'),

    # Resultats
    path('resultats/', views.resultats, name='resultats'),
]
