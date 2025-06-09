from django.urls import path
from .views import list_saida, new_saida

app_name = 'saida'

urlpatterns = [
    path('list_saida', list_saida, name='list_saida'),
    path('new_saida', new_saida, name='new_saida'),
]