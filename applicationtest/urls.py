from django.urls import path
from .views import about, index  # Importation correcte

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
