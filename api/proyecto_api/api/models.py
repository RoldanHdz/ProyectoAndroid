from django.db import models

class Usuario(models.Model):
    nombre = models.TextField()
    email = models.EmailField(unique=True)
    contraseña = models.TextField()
    foto_perfil = models.TextField(null=True, blank=True)
    identificacion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Reporte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.TextField()
    descripcion = models.TextField()
    categoria = models.TextField()
    ubicacion_geografica = models.CharField(max_length=255)  # Usamos CharField para almacenar "POINT(x y)"
    foto_problema = models.JSONField(null=True, blank=True)  # Django 3.1+ soporta JSONField
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    estado = models.TextField()

class Apoyo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    fecha_apoyo = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

class Entidad(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    sitio_web = models.TextField()
    url = models.TextField()
    imagen = models.TextField()

class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_notificacion = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)

class Reaccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    tipo_reaccion = models.TextField()
    fecha_reaccion = models.DateTimeField(auto_now_add=True)

class Seguimiento(models.Model):
    seguidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguidor')
    seguido = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguido')
    fecha_seguimiento = models.DateTimeField(auto_now_add=True)

class HistorialActividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_actividad = models.TextField()
    detalle = models.TextField()
    fecha_actividad = models.DateTimeField(auto_now_add=True)
