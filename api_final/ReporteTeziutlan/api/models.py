from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    foto_id = models.BinaryField()  # Eliminado null=True, blank=True
    foto_perfil = models.BinaryField()  # Eliminado null=True, blank=True
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=[('activo', 'Activo'), ('suspendido', 'Suspendido')], default='activo')

class PerfilUsuario(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    total_reportes = models.IntegerField(default=0)
    total_apoyos = models.IntegerField(default=0)

class Reporte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    ubicacion_latitud = models.FloatField()
    ubicacion_longitud = models.FloatField()
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    foto_reporte = models.BinaryField()  # Eliminado null=True, blank=True
    foto_referencia = models.BinaryField()  # Eliminado null=True, blank=True
    estado_reporte = models.CharField(max_length=20, choices=[('abierto', 'Abierto'), ('en progreso', 'En progreso'), ('cerrado', 'Cerrado')], default='abierto')

class ApoyoEnReporte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    fecha_apoyo = models.DateTimeField(auto_now_add=True)

class ComentarioEnReporte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

class EntidadOficial(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    url_oficial = models.URLField(max_length=255)
