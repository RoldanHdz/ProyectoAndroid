from rest_framework import viewsets
from .models import Usuario, PerfilUsuario, Reporte, ApoyoEnReporte, ComentarioEnReporte, EntidadOficial
from .serializers import UsuarioSerializer, PerfilUsuarioSerializer, ReporteSerializer, ApoyoEnReporteSerializer, ComentarioEnReporteSerializer, EntidadOficialSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ApoyoEnReporteViewSet(viewsets.ModelViewSet):
    queryset = ApoyoEnReporte.objects.all()
    serializer_class = ApoyoEnReporteSerializer

class ComentarioEnReporteViewSet(viewsets.ModelViewSet):
    queryset = ComentarioEnReporte.objects.all()
    serializer_class = ComentarioEnReporteSerializer

class EntidadOficialViewSet(viewsets.ModelViewSet):
    queryset = EntidadOficial.objects.all()
    serializer_class = EntidadOficialSerializer
