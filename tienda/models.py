from django.db import models

from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Desarrolladora(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    sitio_web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class RequisitosSistema(models.Model):
    sistema_operativo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=150)
    memoria_ram = models.CharField(max_length=50)
    tarjeta_grafica = models.CharField(max_length=150)
    almacenamiento = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sistema_operativo} / {self.procesador} / {self.tarjeta_grafica}"

class Juego(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2) # En dólares
    fecha_lanzamiento = models.DateField(blank=True, null=True)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    
    # Relaciones
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE, related_name='juegos')
    plataformas = models.ManyToManyField(Plataforma, related_name='juegos')
    categorias = models.ManyToManyField(Categoria, related_name='juegos')
    requisitos = models.OneToOneField(RequisitosSistema, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Compra(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='compras')
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='compras')
    fecha_compra = models.DateTimeField(auto_now_add=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.usuario.username} compró {self.juego.titulo} por ${self.precio_compra}"
