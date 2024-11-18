from rest_framework import serializers
from .models import Usuario, PerfilUsuario, Reporte, ApoyoEnReporte, ComentarioEnReporte, EntidadOficial

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class ApoyoEnReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApoyoEnReporte
        fields = '__all__'

class ComentarioEnReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioEnReporte
        fields = '__all__'

class EntidadOficialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadOficial
        fields = '__all__'
