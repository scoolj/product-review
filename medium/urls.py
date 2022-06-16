from django.contrib import admin
from django.urls import include, re_path
from reviews.views import ImageViewSet, ProductViewSet 
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'image', ImageViewSet, basename='Image')


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('auth/', include('auth.urls')),
    re_path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
