from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, PerfilUsuarioViewSet, ReporteViewSet, ApoyoEnReporteViewSet, ComentarioEnReporteViewSet, EntidadOficialViewSet


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'perfiles', PerfilUsuarioViewSet)
router.register(r'reportes', ReporteViewSet)
router.register(r'apoyos', ApoyoEnReporteViewSet)
router.register(r'comentarios', ComentarioEnReporteViewSet)
router.register(r'entidades', EntidadOficialViewSet)


urlpatterns = router.urls
