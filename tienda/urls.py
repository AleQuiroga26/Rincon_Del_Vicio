from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('juego/<int:id>/', views.detalle_juego, name='detalle_juego'),
    path('nuevo/', views.crear_juego, name='crear_juego'),
    path('editar/<int:id>/', views.editar_juego, name='editar_juego'),
    path('eliminar/<int:id>/', views.eliminar_juego, name='eliminar_juego'),
    
    # Categorías
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categoria/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
]
