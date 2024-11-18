from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'reportes', ReporteViewSet)
router.register(r'apoyos', ApoyoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'entidades', EntidadViewSet)
router.register(r'notificaciones', NotificacionViewSet)
router.register(r'reacciones', ReaccionViewSet)
router.register(r'seguimientos', SeguimientoViewSet)
router.register(r'historial_actividad', HistorialActividadViewSet)

urlpatterns = router.urls
