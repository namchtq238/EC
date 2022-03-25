from django.urls import include, path
from django.db import router

from .views import ManufViewSet, LaptopViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'laptop', LaptopViewSet, basename="laptop")
router.register(r'manufacture', ManufViewSet, basename="manufacture")


urlpatterns = [
    path('', include(router.urls)),
]