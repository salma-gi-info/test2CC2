# applicationtest/forms.py
from django import forms
from .models import Collec

class CollecForm(forms.ModelForm):
    class Meta:
        model = Collec
        fields = ['title', 'description']  # Exclut 'date' pour l'ajout automatique
