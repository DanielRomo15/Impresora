from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Impresora, Mantenimiento

# --- Impresora ---



def nuevaImpresora(request):
    return render(request, 'nuevaImpresora.html')

def guardarImpresora(request):
    marca = request.POST["marca"]
    propietario = request.POST["propietario"]
    descripcion = request.POST["descripcion"]
    estado = request.POST["estado"]

    Impresora.objects.create(
        marca=marca,
        propietario=propietario,
        descripcion=descripcion,
        estado=estado
    )
    messages.success(request, "Impresora guardada exitosamente")
    return redirect('impresoras')

def eliminarImpresora(request, id):
    impresora = get_object_or_404(Impresora, id=id)
    impresora.delete()
    messages.success(request, "Impresora eliminada exitosamente")
    return redirect('impresoras')

def editarImpresora(request, id):
    impresora = get_object_or_404(Impresora, id=id)
    estados = ['en_proceso', 'finalizado']
    return render(request, 'editarImpresora.html', {
        'impresora': impresora,
        'estados': estados
    })

def procesarEdicionImpresora(request):
    id = request.POST["id"]
    impresora = get_object_or_404(Impresora, id=id)

    impresora.marca = request.POST["marca"]
    impresora.propietario = request.POST["propietario"]
    impresora.descripcion = request.POST["descripcion"]
    impresora.estado = request.POST["estado"]
    impresora.save()

    messages.success(request, "Impresora actualizada exitosamente")
    return redirect('impresoras')

# --- Mantenimiento ---

def mantenimientos(request):
    mantenimientos = Mantenimiento.objects.select_related('impresora').all()
    return render(request, 'mantenimientos.html', {'mantenimientos': mantenimientos})

def nuevoMantenimiento(request):
    impresoras = Impresora.objects.all()
    return render(request, 'nuevoMantenimiento.html', {'impresoras': impresoras})

def guardarMantenimiento(request):
    costo = request.POST["costo"]
    detalles = request.POST["detalles"]
    impresora_id = request.POST["impresora"]

    impresora = get_object_or_404(Impresora, id=impresora_id)

    Mantenimiento.objects.create(
        costo=costo,
        detalles=detalles,
        impresora=impresora
    )
    messages.success(request, "Mantenimiento guardado exitosamente")
    return redirect('mantenimientos')

def eliminarMantenimiento(request, id):
    mantenimiento = get_object_or_404(Mantenimiento, id=id)
    mantenimiento.delete()
    messages.success(request, "Mantenimiento eliminado exitosamente")
    return redirect('mantenimientos')

def editarMantenimiento(request, id):
    mantenimiento = get_object_or_404(Mantenimiento, id=id)
    impresoras = Impresora.objects.all()
    return render(request, 'editarMantenimiento.html', {
        'mantenimiento': mantenimiento,
        'impresoras': impresoras
    })

def procesarEdicionMantenimiento(request):
    id = request.POST["id"]
    mantenimiento = get_object_or_404(Mantenimiento, id=id)

    mantenimiento.costo = request.POST["costo"]
    mantenimiento.detalles = request.POST["detalles"]
    impresora_id = request.POST["impresora"]
    mantenimiento.impresora = get_object_or_404(Impresora, id=impresora_id)
    mantenimiento.save()

    messages.success(request, "Mantenimiento actualizado exitosamente")
    return redirect('mantenimientos')
