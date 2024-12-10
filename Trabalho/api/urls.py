from rest_framework import routers
from .views import ArtistaViewSet, AlbumViewSet, MusicaViewSet

router = routers.DefaultRouter()
router.register(r'artistas', ArtistaViewSet)
router.register(r'albuns', AlbumViewSet)
router.register(r'musicas', MusicaViewSet)

urlpatterns = router.urls