from django.shortcuts import render, get_object_or_404  # Importation en haut
from .models import Collec
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
