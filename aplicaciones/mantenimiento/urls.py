from django.urls import path
from . import views

urlpatterns = [

    # Impresoras
    path('impresoras/', views.impresoras, name='impresoras'),
    path('impresoras/nuevaImpresora/', views.nuevaImpresora, name='nuevaImpresora'),
    path('impresoras/guardarImpresora/', views.guardarImpresora, name='guardarImpresora'),
    path('impresoras/eliminarImpresora/<int:id>/', views.eliminarImpresora, name='eliminarImpresora'),
    path('impresoras/editarImpresora/<int:id>/', views.editarImpresora, name='editarImpresora'),
    path('impresoras/procesarEdicionImpresora/', views.procesarEdicionImpresora, name='procesarEdicionImpresora'),

    # Mantenimientos
    path('mantenimientos/', views.mantenimientos, name='mantenimientos'),
    path('mantenimientos/nuevoMantenimiento/', views.nuevoMantenimiento, name='nuevoMantenimiento'),
    path('mantenimientos/guardarMantenimiento/', views.guardarMantenimiento, name='guardarMantenimiento'),
    path('mantenimientos/eliminarMantenimiento/<int:id>/', views.eliminarMantenimiento, name='eliminarMantenimiento'),
    path('mantenimientos/editarMantenimiento/<int:id>/', views.editarMantenimiento, name='editarMantenimiento'),
    path('mantenimientos/procesarEdicionMantenimiento/', views.procesarEdicionMantenimiento, name='procesarEdicionMantenimiento'),
]
