from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
class Clothes(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=30)
    material = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=CASCADE)
