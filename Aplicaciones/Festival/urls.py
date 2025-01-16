#configuradndo redireccionamineto 
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),# URLs para artistas
    
    path('ListadoArtista/', views.listadoArtista, name='ListadoArtista'),
    path('EliminarArtista/<id>/', views.eliminarArtista, name='EliminarArtista'),
    path('nuevoArtista/', views.nuevoArtista, name='nuevoArtista'),
    path('guardarArtista/', views.guardarArtista, name='guardarArtista'),
    path('editarArtista/<id>/', views.editarArtista, name='editarArtista'),
    path('procesoActualizacionArtista/', views.actualizarArtista, name='procesoActualizacionArtista'),
    
    path('ListadoFestival/', views.listadoFestivales, name='ListadoFestival'),
    
    path('ListadoPresentacion/', views.listadoPresentacion, name='ListadoPresentacion'),
    
    path('ListadoBoleto/', views.listadoBoleto, name='ListadoBoleto'),
    
    path('ListadoCompra/', views.listadoCompra, name='ListadoCompra'),


]



