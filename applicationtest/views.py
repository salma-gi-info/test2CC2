from django.shortcuts import render  # Importation en haut

# Création des vues
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
