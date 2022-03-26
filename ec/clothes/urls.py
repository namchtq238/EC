from django.urls import include, path
from django.db import router

from .views import ClothesList, ClothesDetail, BrandList, BrandDetail

urlpatterns = [
    path('', ClothesList.as_view()),
    path('<int:pk>', ClothesDetail.as_view()),
    path('brand', BrandList.as_view()),
    path('brand/<int:pk>', BrandDetail.as_view()),

    
]
