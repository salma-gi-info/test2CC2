from django.shortcuts import render, get_object_or_404  # Importation en haut
from .models import Collec
from .forms import CollecForm
from django.urls import reverse
# Création des vues
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def collec_detail(request, id):
    collection = get_object_or_404(Collec, id=id)
    return render(request, 'collec_detail.html', {'collection': collection})

def collection_list(request):
    collections = Collec.objects.all()
    return render(request, 'collection_list.html', {'collections': collections})

# applicationtest/views.py
from django.shortcuts import render, redirect
from .forms import CollecForm
from .models import Collec
from datetime import date

def add_collection(request):
    if request.method == 'POST':
        form = CollecForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.date = date.today()  # Définir la date automatiquement
            collection.save()
            return redirect('collection_list')  # Redirige vers la liste des collections
    else:
        form = CollecForm()
    return render(request, 'add_collection.html', {'form': form})

def delete_collection(request, id):
    collection = get_object_or_404(Collec, id=id)
    if request.method == 'POST':
        collection.delete()
        return redirect('collection_list')  # Redirige vers la liste des collections après suppression
    return render(request, 'delete_collection.html', {'collection': collection})


def edit_collection(request, id):
    collection = get_object_or_404(Collec, id=id)
    if request.method == 'POST':
        form = CollecForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect(reverse('collection_list'))
    else:
        form = CollecForm(instance=collection)
    return render(request, 'edit_collection.html', {'form': form, 'collection': collection})