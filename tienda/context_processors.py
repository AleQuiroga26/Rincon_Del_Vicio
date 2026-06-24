from .models import Juego

def total_juegos(request):
    return {
        'total_juegos': Juego.objects.count()
    }
