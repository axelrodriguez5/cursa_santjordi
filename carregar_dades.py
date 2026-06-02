"""
Script opcional per carregar dades de prova.
Per executar-lo:
    python manage.py shell < carregar_dades.py
"""
from cursa.models import Categoria, Participant
import datetime

# Esborrar dades anteriors (opcional)
Participant.objects.all().delete()
Categoria.objects.all().delete()

# Crear categories
c1 = Categoria.objects.create(nom='Infantil', edat_minima=8, edat_maxima=12, distancia_km=2.5)
c2 = Categoria.objects.create(nom='Juvenil', edat_minima=13, edat_maxima=17, distancia_km=5.0)
c3 = Categoria.objects.create(nom='Adult', edat_minima=18, edat_maxima=99, distancia_km=10.0)

# Crear participants
Participant.objects.create(
    nom='Joan', cognoms='Garcia', dorsal=101,
    email='joan@test.cat', data_naixement=datetime.date(2014, 5, 1),
    categoria=c1, temps_segons=720
)
Participant.objects.create(
    nom='Maria', cognoms='Lopez', dorsal=102,
    email='maria@test.cat', data_naixement=datetime.date(2013, 8, 12),
    categoria=c1, temps_segons=680
)
Participant.objects.create(
    nom='Pere', cognoms='Vila', dorsal=201,
    email='pere@test.cat', data_naixement=datetime.date(2008, 3, 10),
    categoria=c2, temps_segons=1500
)
Participant.objects.create(
    nom='Anna', cognoms='Martí', dorsal=301,
    email='anna@test.cat', data_naixement=datetime.date(1990, 7, 22),
    categoria=c3, temps_segons=2700
)

print(f"Categories creades: {Categoria.objects.count()}")
print(f"Participants creats: {Participant.objects.count()}")
