from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Artista, Festival, Presentacion, Boleto, Compra
# VIEWS DE ARTISTA
def home(request):
    return render(request, "home.html")

def listadoArtista(request):
    artista = Artista.objects.all()
    return render(request, "ListadoArtista.html", {'artista': artista})


def nuevoArtista(request):
    return render(request, "nuevoArtista.html")


def guardarArtista(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        biografia = request.POST.get("biografia")
        genero = request.POST.get("genero")
        pais_origen = request.POST.get("pais_origen")
        redes_sociales = request.POST.get("redes_sociales")

        if not all([nombre, biografia, genero, pais_origen, redes_sociales]):
            messages.error(request, "Por favor, complete todos los campos.")
            return redirect('nuevoArtista')

        try:
            Artista.objects.create(
                nombre=nombre,
                biografia=biografia,
                genero=genero,
                pais_origen=pais_origen,
                redes_sociales=redes_sociales
            )
            messages.success(request, "Artista registrado exitosamente.")
            return redirect('listadoArtista')
        except Exception as e:
            messages.error(request, f"Error al guardar el artista: {e}")
            return redirect('nuevoArtista')



def editarArtista(request, id):
    artista = get_object_or_404(Artista, id=id)
    return render(request, "editarArtista.html", {'artista': artista})

def actualizarArtista(request):
    if request.method == 'POST':
        id = request.POST["id"]
        nombre = request.POST["nombre"]
        biografia = request.POST["biografia"]  # Cambiar a 'biografia' si así lo tienes en el modelo
        genero = request.POST["genero"]
        pais_origen = request.POST["pais_origen"]
        redes_sociales = request.POST["redes_sociales"]

        # Obtener el artista por su ID
        artista = get_object_or_404(Artista, id=id)

        # Actualizar los valores del artista
        artista.nombre = nombre
        artista.biografia = biografia  # Asegúrate de que se usa 'biografia' y no 'descripcion'
        artista.genero = genero
        artista.pais_origen = pais_origen
        artista.redes_sociales = redes_sociales
        # Guardar los cambios
        artista.save()

        messages.success(request, "Artista actualizado exitosamente.")
    return redirect('listadoArtista')

def eliminarArtista(request, id):
    artista = get_object_or_404(Artista, id=id)
    artista.delete()
    messages.success(request, "Artista eliminado exitosamente.")
    return redirect('listadoArtista')


# VIEWS DE FESTIVAL
def listadoFestival(request):
    festivales = Festival.objects.all()
    return render(request, "festival/listadoFestival.html", {'festivales': festivales})

def nuevoFestival(request):
    return render(request, "festival/nuevoFestival.html")

def guardarFestival(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        fecha = request.POST["fecha"]
        lugar = request.POST["lugar"]
        Festival.objects.create(nombre=nombre, fecha=fecha, lugar=lugar)
        messages.success(request, "Festival registrado exitosamente.")
    return redirect('listadoFestival')

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
    return redirect('listadoFestival')

def eliminarFestival(request, id):
    festival = get_object_or_404(Festival, id=id)
    festival.delete()
    messages.success(request, "Festival eliminado exitosamente.")
    return redirect('listadoFestival')


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
    return redirect('listadoPresentacion')

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
    return redirect('listadoPresentacion')

def eliminarPresentacion(request, id):
    presentacion = get_object_or_404(Presentacion, id=id)
    presentacion.delete()
    messages.success(request, "Presentación eliminada exitosamente.")
    return redirect('listadoPresentacion')


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
    return redirect('listadoBoleto')

def eliminarBoleto(request, id):
    boleto = get_object_or_404(Boleto, id=id)
    boleto.delete()
    messages.success(request, "Boleto eliminado exitosamente.")
    return redirect('listadoBoleto')


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
    return redirect('listadoCompra')

def eliminarCompra(request, id):
    compra = get_object_or_404(Compra, id=id)
    compra.delete()
    messages.success(request, "Compra eliminada exitosamente.")
    return redirect('listadoCompra')
