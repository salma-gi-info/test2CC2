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