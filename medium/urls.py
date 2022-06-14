from django.contrib import admin
from django.urls import include, re_path
from reviews.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
]
