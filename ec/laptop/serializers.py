from dataclasses import field
from rest_framework import serializers
from .models import Manuf, Laptop

class LaptopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Laptop
        fields = '__all__'
        depth = 1


class ManufSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Manuf
        fields = '__all__'