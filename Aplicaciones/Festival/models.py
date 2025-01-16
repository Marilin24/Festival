from django.db import models
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    genero = models.CharField(max_length=50)  # Este es el campo para el género
    pais_origen = models.CharField(max_length=100)  # Este es el campo para el país de origen
    redes_sociales = models.URLField(max_length=200)

    def __str__(self):
        return self.nombre


class Festival(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    id_organizador = models.IntegerField()

    def __str__(self):
        return self.nombre

class Presentacion(models.Model):
    id_festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    id_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    horario = models.DateTimeField()
    escenario = models.CharField(max_length=100)
    duracion_min = models.IntegerField()

    def __str__(self):
        return f"{self.id_festival.nombre} - {self.id_artista.nombre}"

class Boleto(models.Model):
    id_festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_total = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} - {self.id_festival.nombre}"

class Compra(models.Model):
    id_usuario = models.IntegerField()
    id_boleto = models.ForeignKey(Boleto, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Compra {self.id_usuario} - {self.id_boleto}"
