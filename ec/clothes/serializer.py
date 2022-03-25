from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Brand, Clothes

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['id', 'color', 'material', 'size', 'brand']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'country']