from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Participant, Categoria
from .forms import FormulariParticipant, FormulariCategoria


# --- INDEX ---
def index(request):
    total_participants = Participant.objects.count()
    total_categories = Categoria.objects.count()
    participants_amb_temps = Participant.objects.filter(
        temps_segons__isnull=False
    ).count()
    context = {
        'total_participants': total_participants,
        'total_categories': total_categories,
        'participants_amb_temps': participants_amb_temps,
    }
    return render(request, 'cursa/index.html', context)


# --- PARTICIPANTS ---
def llista_participants(request):
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        participants = Participant.objects.filter(
            categoria_id=categoria_id
        ).order_by('dorsal')
    else:
        participants = Participant.objects.all().order_by('dorsal')

    categories = Categoria.objects.all()
    context = {
        'participants': participants,
        'categories': categories,
        'categoria_seleccionada': categoria_id,
    }
    return render(request, 'cursa/llista_participants.html', context)


def afegir_participant(request):
    if request.method == 'POST':
        form = FormulariParticipant(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant afegit correctament!')
            return redirect('llista_participants')
    else:
        form = FormulariParticipant()
    return render(request, 'cursa/form_participant.html',
                  {'form': form, 'accio': 'Afegir'})


def editar_participant(request, id):
    participant = get_object_or_404(Participant, id=id)
    if request.method == 'POST':
        form = FormulariParticipant(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant actualitzat correctament!')
            return redirect('llista_participants')
    else:
        form = FormulariParticipant(instance=participant)
    return render(request, 'cursa/form_participant.html',
                  {'form': form, 'accio': 'Editar'})


def eliminar_participant(request, id):
    participant = get_object_or_404(Participant, id=id)
    if request.method == 'POST':
        participant.delete()
        messages.success(request, 'Participant eliminat correctament!')
        return redirect('llista_participants')
    return render(request, 'cursa/confirmar_eliminar.html',
                  {'participant': participant})


# --- CATEGORIES ---
def llista_categories(request):
    categories = Categoria.objects.all().order_by('edat_minima')
    return render(request, 'cursa/llista_categories.html',
                  {'categories': categories})


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


# --- RESULTATS ---
def resultats(request):
    # Mostra participants amb temps, ordenats pel temps (els més ràpids primer)
    classificacio = Participant.objects.filter(
        temps_segons__isnull=False
    ).order_by('temps_segons')
    return render(request, 'cursa/resultats.html',
                  {'classificacio': classificacio})
