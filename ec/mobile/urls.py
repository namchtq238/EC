from posixpath import basename
from django.urls import include, path
from django.db import router

from .views import MobileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mobile', MobileViewSet,basename="mobile")

urlpatterns = [
    path('', include(router.urls)),
]