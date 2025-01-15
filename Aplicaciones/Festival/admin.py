# admin.py
from django.contrib import admin
from .models import Artista, Festival, Presentacion, Boleto, Compra

# Registrando los modelos básicos
admin.site.register(Artista)
admin.site.register(Festival)
admin.site.register(Presentacion)
admin.site.register(Boleto)
admin.site.register(Compra)
