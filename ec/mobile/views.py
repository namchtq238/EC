from turtle import screensize
from django.db import connection
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import Mobile
from .serializers import MobileSerializer

class MobileViewSet(viewsets.ModelViewSet):
    serializer_class = MobileSerializer
    
    def get_queryset(self):
        list_mobile = Mobile.objects.all()
        return list_mobile

    def create(self, request, *args, **kwargs):
        data = request.data
        new_mobile =None
        new_mobile = Mobile.objects.create(
          cpu=data['cpu'],
          gpu=data['gpu'],
          storageSize=data['storageSize'],
          screenSize=data['screenSize'],
          screenResolution=data['screenResolution'],
          ramSize=data['ramSize'],
          connection=data['connection'],
          interfaces=data['interfaces'],
          battery=data['battery'],
          os=data['os'],
          frontCamera=data['frontCamera'],
          rearCamera=['rearCamera'],
          speaker=['speaker']
        )
          	
        new_mobile.save()
        serializer = MobileSerializer(new_mobile)
        
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        current_mobile= self.get_object()
        data=request.data
        new_mobile= None
        
        current_mobile.cpu=data['cpu']
        current_mobile.gpu=data['gpu']
        current_mobile.storageSize=data['storageSize']
        current_mobile.screenSize=data['screenSize']
        current_mobile.screenResolution=data['screenResolution']
        current_mobile.ramSize=data['ramSize']
        current_mobile.connection=data['connection']
        current_mobile.interfaces=data['interfaces']
        current_mobile.battery=data['battery']
        current_mobile.os=data['os']
        current_mobile.frontCamera=data['frontCamera']
        current_mobile.rearCamera=['rearCamera']
        current_mobile.speaker=['speaker']

        current_mobile.save()
        
        serializer = MobileSerializer(current_mobile)
        return Response(serializer.data)