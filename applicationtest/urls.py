from django.urls import path
from .views import about, index, collec_detail, collection_list, add_collection,delete_collection  # Importation correcte

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('collection/<int:id>/', collec_detail, name='collec_detail'),
    path('all/', collection_list, name='collection_list'),
    path('new/', add_collection, name='add_collection'),
    path('delete/<int:id>/', delete_collection, name='delete_collection'),
]


