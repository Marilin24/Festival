from os import path
from Aplicaciones.Festival import views

urlpatterns = [
    path('', views.home),
    path('', views.index, name='index'),  # Ruta para el índice
]
