from django.conf.urls.static import static
from django.conf import settings
from applications.file.views import FileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('file', FileViewSet)


urlpatterns = [
    
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)