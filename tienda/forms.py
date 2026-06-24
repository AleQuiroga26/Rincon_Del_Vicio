from django import forms
from .models import Juego, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'descripcion', 'precio', 'fecha_lanzamiento', 'portada', 'desarrolladora', 'plataformas', 'categorias', 'requisitos']
