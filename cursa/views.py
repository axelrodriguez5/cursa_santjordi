"""
Vistes de l'aplicació. Cada funció s'encarrega de respondre a una URL,
consultar dades amb l'ORM i renderitzar una plantilla HTML.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Participant, Categoria
from .forms import FormulariParticipant, FormulariCategoria


# ============================================================
# PÀGINA D'INICI
# Mostra estadístiques generals usant l'ORM (.count() i .filter())
# ============================================================
def index(request):
    # Consultes a la BD amb l'ORM de Django
    total_participants = Participant.objects.count()
    total_categories = Categoria.objects.count()
    participants_amb_temps = Participant.objects.filter(
        temps_segons__isnull=False  # Només els que tenen temps registrat
    ).count()

    # Passem les dades a la plantilla amb un diccionari (context)
    context = {
        'total_participants': total_participants,
        'total_categories': total_categories,
        'participants_amb_temps': participants_amb_temps,
    }
    return render(request, 'cursa/index.html', context)


# ============================================================
# PARTICIPANTS - LLISTAT (amb filtre per categoria)
# ============================================================
def llista_participants(request):
    # Llegim el paràmetre GET ?categoria= de la URL
    categoria_id = request.GET.get('categoria')

    if categoria_id:
        # Filtre amb l'ORM: equivalent a SELECT * FROM participants WHERE categoria_id=...
        participants = Participant.objects.filter(
            categoria_id=categoria_id
        ).order_by('dorsal')
    else:
        # Sense filtre: tots els participants ordenats per dorsal
        participants = Participant.objects.all().order_by('dorsal')

    categories = Categoria.objects.all()  # Per al desplegable del filtre

    context = {
        'participants': participants,
        'categories': categories,
        'categoria_seleccionada': categoria_id,
    }
    return render(request, 'cursa/llista_participants.html', context)


# ============================================================
# PARTICIPANTS - AFEGIR (formulari)
# ============================================================
def afegir_participant(request):
    if request.method == 'POST':
        # L'usuari ha enviat el formulari
        form = FormulariParticipant(request.POST)
        if form.is_valid():
            form.save()  # Guarda el participant a la BD
            # Missatge verd que es mostrarà a la pàgina següent
            messages.success(request, 'Participant afegit correctament!')
            return redirect('llista_participants')
    else:
        # Primera vegada que entra: mostrem el formulari buit
        form = FormulariParticipant()

    return render(request, 'cursa/form_participant.html',
                  {'form': form, 'accio': 'Afegir'})


# ============================================================
# PARTICIPANTS - EDITAR
# ============================================================
def editar_participant(request, id):
    # get_object_or_404: si no existeix l'id, retorna error 404
    participant = get_object_or_404(Participant, id=id)

    if request.method == 'POST':
        # instance=participant -> actualitza l'objecte existent en comptes de crear-ne un de nou
        form = FormulariParticipant(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant actualitzat correctament!')
            return redirect('llista_participants')
    else:
        # Mostrem el formulari precarregat amb les dades actuals
        form = FormulariParticipant(instance=participant)

    return render(request, 'cursa/form_participant.html',
                  {'form': form, 'accio': 'Editar'})


# ============================================================
# PARTICIPANTS - ELIMINAR (amb pantalla de confirmació)
# ============================================================
def eliminar_participant(request, id):
    participant = get_object_or_404(Participant, id=id)

    if request.method == 'POST':
        # Si l'usuari ha confirmat, esborrem
        participant.delete()
        messages.success(request, 'Participant eliminat correctament!')
        return redirect('llista_participants')

    # Si és GET, mostrem la pantalla de confirmació
    return render(request, 'cursa/confirmar_eliminar.html',
                  {'participant': participant})


# ============================================================
# CATEGORIES - LLISTAT
# ============================================================
def llista_categories(request):
    # order_by ordena per edat mínima (de més petita a més gran)
    categories = Categoria.objects.all().order_by('edat_minima')
    return render(request, 'cursa/llista_categories.html',
                  {'categories': categories})


# ============================================================
# CATEGORIES - AFEGIR
# ============================================================
def afegir_categoria(request):
    if request.method == 'POST':
        form = FormulariCategoria(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria afegida correctament!')
            return redirect('llista_categories')
    else:
        form = FormulariCategoria()

    return render(request, 'cursa/form_categoria.html',
                  {'form': form, 'accio': 'Afegir'})


# ============================================================
# RESULTATS - Classificació general ordenada per temps
# ============================================================
def resultats(request):
    # Filtrem els que tenen temps + ordenem ascendentment (els més ràpids primer)
    classificacio = Participant.objects.filter(
        temps_segons__isnull=False
    ).order_by('temps_segons')

    return render(request, 'cursa/resultats.html',
                  {'classificacio': classificacio})