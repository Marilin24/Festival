from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Artista, Festival, Presentacion, Boleto, Compra
# VIEWS DE ARTISTA
def home(request):
    return render(request, "home.html")

def listadoArtista(request):
    artista = Artista.objects.all()
    return render(request, "artista/ListadoArtista.html", {'artista': artista})

def nuevoArtista(request):
    return render(request, "artista/nuevoArtista.html")

def guardarArtista(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        foto = request.FILES.get("foto")
        Artista.objects.create(nombre=nombre, descripcion=descripcion, foto=foto)
        messages.success(request, "Artista registrado exitosamente.")
    return redirect('listadoArtistas')

def editarArtista(request, id):
    artista = get_object_or_404(Artista, id=id)
    return render(request, "artista/editarArtista.html", {'artista': artista})

def actualizarArtista(request):
    if request.method == 'POST':
        id = request.POST["id"]
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        artista = get_object_or_404(Artista, id=id)
        artista.nombre = nombre
        artista.descripcion = descripcion
        artista.save()
        messages.success(request, "Artista actualizado exitosamente.")
    return redirect('listadoArtistas')

def eliminarArtista(request, id):
    artista = get_object_or_404(Artista, id=id)
    artista.delete()
    messages.success(request, "Artista eliminado exitosamente.")
    return redirect('listadoArtistas')


# VIEWS DE FESTIVAL
def listadoFestivales(request):
    festivales = Festival.objects.all()
    return render(request, "festival/listadoFestivales.html", {'festivales': festivales})

def nuevoFestival(request):
    return render(request, "festival/nuevoFestival.html")

def guardarFestival(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        fecha = request.POST["fecha"]
        lugar = request.POST["lugar"]
        Festival.objects.create(nombre=nombre, fecha=fecha, lugar=lugar)
        messages.success(request, "Festival registrado exitosamente.")
    return redirect('listadoFestivales')

def editarFestival(request, id):
    festival = get_object_or_404(Festival, id=id)
    return render(request, "festival/editarFestival.html", {'festival': festival})

def actualizarFestival(request):
    if request.method == 'POST':
        id = request.POST["id"]
        nombre = request.POST["nombre"]
        fecha = request.POST["fecha"]
        lugar = request.POST["lugar"]
        festival = get_object_or_404(Festival, id=id)
        festival.nombre = nombre
        festival.fecha = fecha
        festival.lugar = lugar
        festival.save()
        messages.success(request, "Festival actualizado exitosamente.")
    return redirect('listadoFestivales')

def eliminarFestival(request, id):
    festival = get_object_or_404(Festival, id=id)
    festival.delete()
    messages.success(request, "Festival eliminado exitosamente.")
    return redirect('listadoFestivales')


# VIEWS DE PRESENTACION
def listadoPresentacion(request):
    presentacion = Presentacion.objects.all()
    return render(request, "presentacion/listadoPresentacion.html", {'presentacion': presentacion})

def nuevaPresentacion(request):
    return render(request, "presentacion/nuevaPresentacion.html")

def guardarPresentacion(request):
    if request.method == 'POST':
        artista_id = request.POST["artista_id"]
        festival_id = request.POST["festival_id"]
        hora = request.POST["hora"]
        Presentacion.objects.create(
            artista_id=artista_id,
            festival_id=festival_id,
            hora=hora,
        )
        messages.success(request, "Presentación registrada exitosamente.")
    return redirect('listadoPresentaciones')

def editarPresentacion(request, id):
    presentacion = get_object_or_404(Presentacion, id=id)
    return render(request, "presentacion/editarPresentacion.html", {'presentacion': presentacion})

def actualizarPresentacion(request):
    if request.method == 'POST':
        id = request.POST["id"]
        artista_id = request.POST["artista_id"]
        festival_id = request.POST["festival_id"]
        hora = request.POST["hora"]
        presentacion = get_object_or_404(Presentacion, id=id)
        presentacion.artista_id = artista_id
        presentacion.festival_id = festival_id
        presentacion.hora = hora
        presentacion.save()
        messages.success(request, "Presentación actualizada exitosamente.")
    return redirect('listadoPresentaciones')

def eliminarPresentacion(request, id):
    presentacion = get_object_or_404(Presentacion, id=id)
    presentacion.delete()
    messages.success(request, "Presentación eliminada exitosamente.")
    return redirect('listadoPresentaciones')


# VIEWS DE BOLETO
def listadoBoleto(request):
    boleto = Boleto.objects.all()
    return render(request, "boleto/listadoBoleto.html", {'boleto': boleto})

def nuevoBoleto(request):
    return render(request, "boleto/nuevoBoleto.html")

def guardarBoleto(request):
    if request.method == 'POST':
        precio = request.POST["precio"]
        tipo = request.POST["tipo"]
        Boleto.objects.create(precio=precio, tipo=tipo)
        messages.success(request, "Boleto registrado exitosamente.")
    return redirect('listadoBoletos')

def eliminarBoleto(request, id):
    boleto = get_object_or_404(Boleto, id=id)
    boleto.delete()
    messages.success(request, "Boleto eliminado exitosamente.")
    return redirect('listadoBoletos')


# VIEWS DE COMPRA
def listadoCompra(request):
    compra = Compra.objects.all()
    return render(request, "compra/listadoCompra.html", {'compra': compra})

def nuevaCompra(request):
    return render(request, "compra/nuevaCompra.html")

def guardarCompra(request):
    if request.method == 'POST':
        boleto_id = request.POST["boleto_id"]
        usuario_id = request.POST["usuario_id"]
        fecha = request.POST["fecha"]
        Compra.objects.create(boleto_id=boleto_id, usuario_id=usuario_id, fecha=fecha)
        messages.success(request, "Compra registrada exitosamente.")
    return redirect('listadoCompras')

def eliminarCompra(request, id):
    compra = get_object_or_404(Compra, id=id)
    compra.delete()
    messages.success(request, "Compra eliminada exitosamente.")
    return redirect('listadoCompras')
